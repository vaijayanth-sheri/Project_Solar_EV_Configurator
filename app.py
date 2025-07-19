import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from modules import location, map_draw, irradiance, sizing, finance, ev, battery, report, self_consumption
from i18n.lang_dict import TEXT

st.set_page_config(page_title="Solar Configurator", page_icon="☀️", layout="wide", initial_sidebar_state="expanded")

# --- Initialize session state with all possible overrides ---
override_keys = ['override_tilt', 'override_azimuth', 'override_losses', 'override_degradation', 'override_panel_density', 'override_lifetime', 'override_cost_per_kwp', 'override_electricity_price', 'override_feed_in_tariff', 'override_battery_cost']
base_keys = ['lang', 'address', 'location_data', 'total_area', 'polygons', 'pvgis_data', 'analysis_complete', 'add_ev', 'num_evs', 'daily_km', 'charger_type', 'add_battery', 'battery_kwh', 'self_consumption_mode', 'annual_kwh_consumption', 'self_consumption_pct', 'report_include_addons', 'report_include_sustainability']
for key in base_keys + override_keys:
    if key not in st.session_state:
        defaults = {
            'lang': 'en', 'address': '', 'location_data': None, 'total_area': 0.0, 'polygons': [], 'pvgis_data': None, 
            'analysis_complete': False, 'add_ev': False, 'num_evs': 1, 'daily_km': 50, 'charger_type': 'AC 11kW', 
            'add_battery': False, 'battery_kwh': 10.0, 'self_consumption_mode': 'annual_kwh', 'annual_kwh_consumption': 4000, 
            'self_consumption_pct': 30, 'report_include_addons': True, 'report_include_sustainability': True
        }
        st.session_state[key] = defaults.get(key, None)

def get_text(key): return TEXT.get(key, {}).get(st.session_state.lang, key)
def load_css(file_name):
    with open(file_name) as f: st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("assets/styles.css")

with st.sidebar:
    st.title(get_text('app_title'))
    lang_options = {'English': 'en', 'Deutsch': 'de'}
    selected_lang_label = [k for k, v in lang_options.items() if v == st.session_state.lang][0]
    new_lang_label = st.selectbox(get_text('language'), options=lang_options.keys(), index=list(lang_options.keys()).index(selected_lang_label))
    st.session_state.lang = lang_options[new_lang_label]
    selected_page = option_menu(menu_title=None, options=[get_text('nav_location'), get_text('nav_rooftop'), get_text('nav_analysis'), get_text('nav_report')], icons=['geo-alt-fill', 'rulers', 'bar-chart-line-fill', 'file-earmark-pdf-fill'], default_index=0)
    st.markdown("---")
    about_button = st.button(get_text('about_header'), use_container_width=True)

st.header(get_text('app_header'))

if about_button:
    st.subheader(get_text('about_tech_title'))
    st.info(get_text('about_tech_text'))
    
    with st.form(key='expert_settings_form'):
        with st.expander(get_text('cat_location'), expanded=True):
             tilt = st.number_input(get_text('form_tilt'), value=st.session_state.override_tilt or irradiance.DEFAULT_TILT, min_value=0.0, max_value=90.0, step=1.0)
             azimuth = st.number_input(get_text('form_orientation'), value=st.session_state.override_azimuth or irradiance.DEFAULT_AZIMUTH, min_value=-180.0, max_value=180.0, step=5.0, help="-180 to 180 (0=South, -90=East, 90=West)")
        
        with st.expander(get_text('cat_irradiance')):
             losses = st.slider(get_text('form_losses'), min_value=0.0, max_value=50.0, value=st.session_state.override_losses or irradiance.DEFAULT_LOSS, step=0.5, format="%.1f%%")
             degradation = st.slider(get_text('form_degradation'), min_value=0.0, max_value=2.0, value=(st.session_state.override_degradation or sizing.DEFAULT_DEGRADATION_RATE) * 100, step=0.05, format="%.2f%%")
        
        with st.expander(get_text('cat_system')):
             panel_density_m2_per_kwp = 1 / (st.session_state.override_panel_density or sizing.DEFAULT_PANEL_DENSITY_KWP_PER_M2)
             panel_density = st.number_input(get_text('form_panel_density'), value=panel_density_m2_per_kwp, min_value=4.0, max_value=10.0, step=0.1, format="%.2f")
             st.text_input("Module Type", placeholder=get_text('form_placeholder_soon'), disabled=True)

        with st.expander(get_text('cat_financial')):
             cost_kwp = st.number_input(get_text('about_form_system_cost'), value=st.session_state.override_cost_per_kwp or finance.DEFAULT_SYSTEM_COST_PER_KWP, step=50.0)
             elec_price = st.number_input(get_text('about_form_electricity_price'), value=st.session_state.override_electricity_price or finance.DEFAULT_ELECTRICITY_PRICE_SAVED, step=0.01, format="%.2f")
             feed_in = st.number_input(get_text('about_form_feed_in_tariff'), value=st.session_state.override_feed_in_tariff or finance.DEFAULT_FEED_IN_TARIFF, step=0.001, format="%.4f")
             batt_cost = st.number_input(get_text('about_form_battery_cost'), value=st.session_state.override_battery_cost or battery.DEFAULT_BATTERY_COST_PER_KWH, step=25.0)
             lifetime = st.number_input(get_text('form_system_lifetime'), value=st.session_state.override_lifetime or finance.DEFAULT_LIFETIME, min_value=10.0, max_value=40.0, step=1.0)

        submitted = st.form_submit_button(get_text('about_form_save_button'))
        if submitted:
            st.session_state.override_tilt, st.session_state.override_azimuth, st.session_state.override_losses = tilt, azimuth, losses
            st.session_state.override_degradation, st.session_state.override_panel_density = degradation / 100.0, 1 / panel_density
            st.session_state.override_cost_per_kwp, st.session_state.override_electricity_price = cost_kwp, elec_price
            st.session_state.override_feed_in_tariff, st.session_state.override_battery_cost = feed_in, batt_cost
            st.session_state.override_lifetime = lifetime
            st.session_state.pvgis_data = None
            st.success(get_text('about_form_success'))
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
                    st.session_state.pvgis_data = irradiance.fetch_pvgis_data(st.session_state.location_data['latitude'], st.session_state.location_data['longitude'], loss_override=st.session_state.override_losses, tilt_override=st.session_state.override_tilt, azimuth_override=st.session_state.override_azimuth)
                    if not st.session_state.pvgis_data:
                        st.error(get_text('error_pvgis_fail'))
                        st.stop()
            
            st.header(get_text('addons_header'))
            with st.expander(get_text('ev_charger_option'), expanded=st.session_state.add_ev):
                st.checkbox("Enable EV Planning", key="add_ev")
                if st.session_state.add_ev:
                    col1, col2, col3 = st.columns(3)
                    col1.number_input("Number of EVs", min_value=1, max_value=3, step=1, key="num_evs")
                    col2.slider("Daily distance per EV (km)", 10, 150, key="daily_km")
                    col3.selectbox("Charger type", ["AC 11kW", "AC 22kW", "DC 50kW"], key="charger_type")
            with st.expander(get_text('battery_option'), expanded=st.session_state.add_battery):
                st.checkbox("Enable Battery", key="add_battery")
                if st.session_state.add_battery:
                    st.slider("Battery size (kWh)", 3.0, 30.0, step=0.5, key="battery_kwh")
            with st.expander(get_text('sc_header'), expanded=True):
                sc_mode = st.radio(get_text('sc_input_mode'), options=['annual_kwh', 'percentage'], format_func=lambda x: get_text(f'sc_mode_{x}'), key='self_consumption_mode')
                if sc_mode == 'annual_kwh':
                    st.number_input(get_text('sc_annual_label'), min_value=0, step=100, key='annual_kwh_consumption')
                else:
                    st.slider(get_text('sc_percentage_label'), min_value=0, max_value=100, step=5, key='self_consumption_pct', format="%d%%")
            
            st.markdown("---")
            st.header(get_text('analysis_header'))
            st.session_state.analysis_complete = True
            
            base_kwp, _ = sizing.calculate_max_system_size(st.session_state.total_area, st.session_state.override_panel_density)
            base_yield = sizing.calculate_energy_output(base_kwp, st.session_state.pvgis_data['total_yearly_kwh'], st.session_state.override_degradation)
            ev_reqs = ev.calculate_ev_requirements(st.session_state.num_evs, st.session_state.daily_km, base_yield) if st.session_state.add_ev else {"extra_kwp_needed": 0, "is_sufficient": True}
            total_kwp = base_kwp + ev_reqs["extra_kwp_needed"]
            total_yield = sizing.calculate_energy_output(total_kwp, st.session_state.pvgis_data['total_yearly_kwh'], st.session_state.override_degradation)
            sc_results = self_consumption.calculate_self_consumption(total_yield, st.session_state.self_consumption_mode, st.session_state.annual_kwh_consumption, st.session_state.self_consumption_pct)
            st.session_state.final_sc = sc_results
            battery_cost = battery.calculate_battery_cost(st.session_state.battery_kwh, st.session_state.override_battery_cost) if st.session_state.add_battery else 0
            
            financials = finance.calculate_financials(system_kwp=total_kwp, self_consumed_kwh=sc_results['self_consumed_kwh'], grid_exported_kwh=sc_results['grid_exported_kwh'], battery_cost=battery_cost, cost_per_kwp_override=st.session_state.override_cost_per_kwp, electricity_price_override=st.session_state.override_electricity_price, feed_in_tariff_override=st.session_state.override_feed_in_tariff, lifetime_override=st.session_state.override_lifetime)
            
            st.session_state.final_financials, st.session_state.final_sizing = financials, {'kwp': total_kwp, 'panels': sizing.calculate_system_details(total_kwp)[0], 'yield': total_yield, 'area': st.session_state.total_area}
            
            st.subheader(get_text('total_system_header'))
            st.metric(get_text('total_system_size'), f"{total_kwp:.2f} kWp")
            st.metric(get_text('total_yearly_yield'), f"{total_yield:,.0f} kWh")
            
            st.markdown(f"### {get_text('financial_subheader')}")
            col1, col2, col3 = st.columns(3)
            col1.metric(get_text('est_system_cost'), f"€ {financials.get('total_cost', 0):,.2f}")
            col2.metric(get_text('total_annual_benefit'), f"€ {financials.get('total_annual_benefit', 0):,.2f}", help=f"Savings: €{financials.get('annual_savings', 0):,.2f} + Feed-in: €{financials.get('annual_feed_in', 0):,.2f}")
            col3.metric(get_text('payback_period'), f"{financials.get('payback_period', 0)} {get_text('years')}")

    elif selected_page == get_text('nav_report'):
        st.subheader(f"📄 4. {get_text('nav_report')}")
        if not st.session_state.analysis_complete: st.warning(get_text('warning_analysis_incomplete'))
        else:
            st.subheader(get_text('cat_report'))
            st.checkbox(get_text('report_include_addons'), key='report_include_addons')
            st.checkbox(get_text('report_include_sustainability'), key='report_include_sustainability')
            st.markdown("---")
            st.success("Your analysis is complete. You can now generate your report.")

            if st.button(get_text('generate_report_button')):
                with st.spinner("Generating PDF..."):
                    pdf_path = report.generate(
                        session_data=st.session_state,
                        text=TEXT,
                        lang=st.session_state.lang
                    )
                    if pdf_path:
                        with open(pdf_path, "rb") as file: 
                            st.download_button(label=get_text('download_report_button'), data=file, file_name="Solar_Configurator_Report.pdf", mime="application/pdf")
                    else: 
                        st.error(get_text('error_pdf_fail'))
