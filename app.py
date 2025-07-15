import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import pandas as pd
import sys
import os

# --- ROBUST PATHING ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from modules import location, map_draw, irradiance, sizing, finance, ev, battery, report
from i18n.lang_dict import TEXT

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Solar Configurator", page_icon="☀️", layout="wide", initial_sidebar_state="expanded")

# --- INITIALIZE SESSION STATE ---
for key in ['lang', 'address', 'location_data', 'total_area', 'polygons', 'pvgis_data', 'analysis_complete', 'add_ev', 'num_evs', 'daily_km', 'charger_type', 'add_battery', 'battery_kwh']:
    if key not in st.session_state:
        defaults = {'lang': 'en', 'address': '', 'location_data': None, 'total_area': 0.0, 'polygons': [], 'pvgis_data': None, 'analysis_complete': False, 'add_ev': False, 'num_evs': 1, 'daily_km': 50, 'charger_type': 'AC 11kW', 'add_battery': False, 'battery_kwh': 10.0}
        st.session_state[key] = defaults.get(key, None)

# --- HELPER FUNCTIONS ---
def get_text(key): return TEXT[key][st.session_state.lang]
def load_css(file_name):
    with open(file_name) as f: st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- UI & LOGIC ---
load_css("assets/styles.css")

# --- SIDEBAR & HEADER ---
with st.sidebar:
    st.title(get_text('app_title'))
    lang_options = {'English': 'en', 'Deutsch': 'de'}
    selected_lang_label = [k for k, v in lang_options.items() if v == st.session_state.lang][0]
    new_lang_label = st.selectbox(get_text('language'), options=lang_options.keys(), index=list(lang_options.keys()).index(selected_lang_label))
    st.session_state.lang = lang_options[new_lang_label]
    
    # Primary workflow navigation
    selected_page = option_menu(menu_title=None, options=[get_text('nav_location'), get_text('nav_rooftop'), get_text('nav_analysis'), get_text('nav_report')], icons=['geo-alt-fill', 'rulers', 'bar-chart-line-fill', 'file-earmark-pdf-fill'], default_index=0)
    
    st.markdown("---")
    # New button to trigger the "About" page
    about_button = st.button(get_text('about_header'), use_container_width=True)

st.header(get_text('app_header'))


# --- MAIN PANEL LAYOUT (CONDITIONAL) ---
if about_button:
    # --- RENDER ABOUT PAGE ---
    st.subheader(get_text('about_header'))
    st.markdown("---")

    st.subheader(get_text('about_overview_title'))
    st.markdown(get_text('about_overview_text'))
    
    st.subheader(get_text('about_tech_title'))
    st.markdown(get_text('about_tech_text'), unsafe_allow_html=True)
    
    st.subheader(get_text('about_limits_title'))
    st.markdown(get_text('about_limits_text'))
    
    st.subheader(get_text('about_future_title'))
    st.markdown(get_text('about_future_text'), unsafe_allow_html=True)

else:
    # --- RENDER NORMAL WORKFLOW ---
    if selected_page == get_text('nav_location'):
        st.subheader(f"📍 1. {get_text('nav_location')}")
        address = st.text_input(get_text('address_input_label'), value=st.session_state.address)
        if st.button(get_text('geocode_button')):
            if address:
                with st.spinner("Finding location..."):
                    st.session_state.address = address
                    st.session_state.location_data = location.geocode_address(address)
                    st.session_state.total_area = 0.0
                    st.session_state.analysis_complete = False
                    st.session_state.pvgis_data = None
                    if st.session_state.location_data: st.success(f"{get_text('geocode_success')}: {st.session_state.location_data['address']}")
                    else: st.error(get_text('geocode_error'))
            else: st.warning("Please enter an address.")
        if st.session_state.location_data: st.map(pd.DataFrame([st.session_state.location_data], columns=['latitude', 'longitude']), zoom=14)

    elif selected_page == get_text('nav_rooftop'):
        st.subheader(f"✏️ 2. {get_text('nav_rooftop')}")
        if not st.session_state.location_data: st.warning(get_text('warning_need_location'))
        else:
            st.info(get_text('rooftop_instruction'))
            m = map_draw.display_map(st.session_state.location_data['latitude'], st.session_state.location_data['longitude'])
            map_data = st_folium(m, width=1200, height=500, key="folium_map")
            total_area = 0
            if map_data and map_data.get("all_drawings"):
                if map_data["all_drawings"]:
                    st.session_state.polygons = map_data["all_drawings"]
                    for p in map_data["all_drawings"]: total_area += map_draw.calculate_polygon_area(p)
            if st.session_state.total_area != total_area:
                st.session_state.total_area = total_area
                st.session_state.analysis_complete = False
                st.rerun()
            st.metric(get_text('total_roof_area'), f"{st.session_state.total_area:.2f} m²")

    elif selected_page == get_text('nav_analysis'):
        st.subheader(f"📊 3. {get_text('nav_analysis')}")
        if st.session_state.total_area <= 0: st.warning(get_text('warning_need_rooftop'))
        else:
            if not st.session_state.pvgis_data:
                with st.spinner("Fetching base solar data..."):
                    st.session_state.pvgis_data = irradiance.fetch_pvgis_data(st.session_state.location_data['latitude'], st.session_state.location_data['longitude'])
                    if not st.session_state.pvgis_data:
                        st.error(get_text('error_pvgis_fail'))
                        st.stop()
            
            st.header(get_text('addons_header'))
            with st.expander(get_text('ev_charger_option'), expanded=st.session_state.add_ev):
                st.checkbox("Enable EV Planning", key="add_ev")
                if st.session_state.add_ev:
                    col1, col2, col3 = st.columns(3)
                    col1.number_input(get_text('num_evs'), min_value=1, max_value=3, step=1, key="num_evs")
                    col2.slider(get_text('daily_driving_distance'), 10, 150, key="daily_km")
                    col3.selectbox(get_text('charger_type'), ["AC 11kW", "AC 22kW", "DC 50kW"], key="charger_type")
            with st.expander(get_text('battery_option'), expanded=st.session_state.add_battery):
                st.checkbox("Enable Battery", key="add_battery")
                if st.session_state.add_battery:
                    st.slider(get_text('battery_capacity'), 3.0, 30.0, step=0.5, key="battery_kwh")

            st.markdown("---")
            st.header(get_text('analysis_header'))
            st.session_state.analysis_complete = True
            base_kwp, base_panel_count = sizing.calculate_max_system_size(st.session_state.total_area)
            base_yield = sizing.calculate_energy_output(base_kwp, st.session_state.pvgis_data['total_yearly_kwh'])
            ev_reqs = {"extra_kwp_needed": 0, "is_sufficient": True}
            if st.session_state.add_ev: ev_reqs = ev.calculate_ev_requirements(st.session_state.num_evs, st.session_state.daily_km, base_yield)
            battery_cost = battery.calculate_battery_cost(st.session_state.battery_kwh) if st.session_state.add_battery else 0
            total_kwp = base_kwp + ev_reqs["extra_kwp_needed"]
            total_yield = sizing.calculate_energy_output(total_kwp, st.session_state.pvgis_data['total_yearly_kwh'])
            financials = finance.calculate_financials(total_kwp, total_yield, battery_cost)
            st.session_state.final_sizing = {'kwp': total_kwp, 'panels': sizing.calculate_system_details(total_kwp)[0], 'yield': total_yield, 'area': st.session_state.total_area}
            st.session_state.final_financials = {'cost': financials['total_cost'], 'savings': financials['yearly_savings'], 'payback': financials['payback_period']}
            st.subheader(get_text('total_system_header'))
            st.metric(get_text('total_system_size'), f"{total_kwp:.2f} kWp", delta=f'{ev_reqs["extra_kwp_needed"]:.2f} kWp for EV' if st.session_state.add_ev and not ev_reqs["is_sufficient"] else None)
            if st.session_state.add_ev and ev_reqs["is_sufficient"]: st.success(get_text('ev_sufficient_msg'))
            st.metric(get_text('total_yearly_yield'), f"{total_yield:,.0f} kWh")
            st.markdown(f"### {get_text('financial_subheader')}")
            col1, col2, col3 = st.columns(3)
            col1.metric(get_text('est_system_cost'), f"€ {financials.get('total_cost', 0):,.2f}")
            col2.metric(get_text('est_yearly_savings'), f"€ {financials.get('yearly_savings', 0):,.2f}")
            col3.metric(get_text('payback_period'), f"{financials.get('payback_period', 0)} {get_text('years')}")

    elif selected_page == get_text('nav_report'):
        st.subheader(f"📄 4. {get_text('nav_report')}")
        if not st.session_state.analysis_complete: st.warning(get_text('warning_analysis_incomplete'))
        else:
            st.success("Your analysis is complete. You can now generate your report.")
            if st.button(get_text('generate_report_button')):
                sizing_data = st.session_state.final_sizing
                financials_data = st.session_state.final_financials
                ev_data = None
                if st.session_state.add_ev:
                    base_yield = sizing.calculate_energy_output(sizing.calculate_max_system_size(st.session_state.total_area)[0], st.session_state.pvgis_data['total_yearly_kwh'])
                    ev_reqs = ev.calculate_ev_requirements(st.session_state.num_evs, st.session_state.daily_km, base_yield)
                    ev_data = {'count': st.session_state.num_evs, 'daily_km': st.session_state.daily_km, 'charger': st.session_state.charger_type, 'kwh_daily': ev_reqs['daily_need_kwh'], 'extra_kwp': ev_reqs['extra_kwp_needed']}
                battery_data = None
                if st.session_state.add_battery: battery_data = {'size': st.session_state.battery_kwh, 'cost': battery.calculate_battery_cost(st.session_state.battery_kwh)}
                with st.spinner("Generating PDF..."):
                    pdf_path = report.generate(polygons=st.session_state.get('polygons', []), sizing=sizing_data, financials=financials_data, location=st.session_state.location_data, pvgis=st.session_state.pvgis_data, ev=ev_data, battery=battery_data, text=TEXT, lang=st.session_state.lang)
                    if pdf_path:
                        with open(pdf_path, "rb") as file: st.download_button(label=get_text('download_report_button'), data=file, file_name="Solar_Configurator_Report.pdf", mime="application/pdf")
                    else: st.error(get_text('error_pdf_fail'))