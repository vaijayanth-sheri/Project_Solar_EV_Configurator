import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.lib import colors

# Import modules to access their default constants for comparison
from modules import irradiance, sizing, finance, battery, ev

primary_color = colors.HexColor('#2E7D32')
text_color = colors.HexColor('#37474F')

def _add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawString(inch, 0.75 * inch, f"Page {doc.page} | Solar Configurator Report")
    canvas.restoreState()

def _format_value(session_data, override_key, default_value, unit="", fmt="{:.2f}", is_percent=False):
    """Helper to format values and indicate if they are custom or default."""
    value = session_data.get(override_key)
    tag_key = 'pdf_custom' if value is not None else 'pdf_default'
    val_to_format = value if value is not None else default_value
    
    if is_percent and val_to_format is not None:
        val_to_format *= 100
        
    return f"{fmt.format(val_to_format)} {unit} ({session_data['get_text'](tag_key)})"

def generate(session_data: dict, text: dict, lang: str) -> str or None:
    filename = "output/solar_report.pdf"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CoverTitle', fontName='Helvetica-Bold', fontSize=28, alignment=TA_CENTER, textColor=primary_color, spaceAfter=20))
    styles.add(ParagraphStyle(name='H1', fontName='Helvetica-Bold', fontSize=16, alignment=TA_LEFT, textColor=primary_color, spaceBefore=20, spaceAfter=10))
    styles.add(ParagraphStyle(name='Body', fontName='Helvetica', fontSize=10, alignment=TA_LEFT, textColor=text_color, leading=14))
    styles.add(ParagraphStyle(name='BodyBold', fontName='Helvetica-Bold', fontSize=10, alignment=TA_LEFT, textColor=text_color, leading=14))
    
    def get_text(key): return text.get(key, {}).get(lang, key)
    session_data['get_text'] = get_text

    story = []
    
    # --- Cover Page ---
    story.append(Paragraph(get_text('pdf_title'), styles['CoverTitle']))
    story.append(Spacer(1, 1 * inch))
    sizing_data = session_data.get('final_sizing', {})
    story.append(Table([
        [Paragraph('<b>Location</b>', styles['Body']), Paragraph(session_data.get('location_data', {}).get('address', 'N/A'), styles['Body'])],
        [Paragraph('<b>Report Date</b>', styles['Body']), Paragraph(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), styles['Body'])],
        [Paragraph('<b>Total System Size</b>', styles['Body']), f"{sizing_data.get('kwp', 0):.2f} kWp"],
        [Paragraph('<b>Est. Annual Yield (Year 1)</b>', styles['Body']), f"{sizing_data.get('yield', 0):,.0f} kWh"],
    ], colWidths=[2.5 * inch, 4.0 * inch], style=[('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(PageBreak())

    # --- Expert Settings Summary ---
    story.append(Paragraph(get_text('pdf_expert_settings_summary'), styles['H1']))
    story.append(Paragraph(get_text('pdf_custom_value_info'), styles['Body']))
    story.append(Spacer(1, 0.2 * inch))
    settings_data = [
        [Paragraph(get_text('form_tilt'), styles['Body']), Paragraph(_format_value(session_data, 'override_tilt', irradiance.DEFAULT_TILT, "°"), styles['Body'])],
        [Paragraph(get_text('form_orientation'), styles['Body']), Paragraph(_format_value(session_data, 'override_azimuth', irradiance.DEFAULT_AZIMUTH, "°"), styles['Body'])],
        [Paragraph(get_text('form_losses'), styles['Body']), Paragraph(_format_value(session_data, 'override_losses', irradiance.DEFAULT_LOSS, "%"), styles['Body'])],
        [Paragraph(get_text('form_degradation'), styles['Body']), Paragraph(_format_value(session_data, 'override_degradation', sizing.DEFAULT_DEGRADATION_RATE, "%", fmt="{:.2f}", is_percent=True), styles['Body'])],
        [Paragraph(get_text('about_form_system_cost'), styles['Body']), Paragraph(_format_value(session_data, 'override_cost_per_kwp', finance.DEFAULT_SYSTEM_COST_PER_KWP, "€/kWp"), styles['Body'])],
        [Paragraph(get_text('about_form_electricity_price'), styles['Body']), Paragraph(_format_value(session_data, 'override_electricity_price', finance.DEFAULT_ELECTRICITY_PRICE_SAVED, "€/kWh", fmt="{:.3f}"), styles['Body'])],
        [Paragraph(get_text('about_form_feed_in_tariff'), styles['Body']), Paragraph(_format_value(session_data, 'override_feed_in_tariff', finance.DEFAULT_FEED_IN_TARIFF, "€/kWh", fmt="{:.4f}"), styles['Body'])],
        [Paragraph(get_text('about_form_battery_cost'), styles['Body']), Paragraph(_format_value(session_data, 'override_battery_cost', battery.DEFAULT_BATTERY_COST_PER_KWH, "€/kWh"), styles['Body'])],
    ]
    story.append(Table(settings_data, colWidths=[3 * inch, 3.5 * inch]))

    # --- System Sizing Summary ---
    story.append(Paragraph(get_text('pdf_spec_title'), styles['H1']))
    story.append(Table([[Paragraph(get_text('pdf_usable_area'), styles['BodyBold']), Paragraph(f"{sizing_data.get('area', 0):.2f} m²", styles['Body'])], [Paragraph(get_text('total_system_size'), styles['BodyBold']), Paragraph(f"<b>{sizing_data.get('kwp', 0):.2f} kWp</b>", styles['Body'])], [Paragraph(get_text('pdf_panel_count'), styles['BodyBold']), Paragraph(f"~ {sizing_data.get('panels', 0)}", styles['Body'])], [Paragraph(get_text('pdf_yield_year_1'), styles['BodyBold']), Paragraph(f"<b>{sizing_data.get('yield', 0):,.0f} kWh/year</b>", styles['Body'])]], colWidths=[3 * inch, 3.5 * inch]))

    # --- Financial Summary ---
    financials_data = session_data.get('final_financials', {})
    story.append(Paragraph(get_text('financial_subheader'), styles['H1']))
    story.append(Table([[Paragraph(get_text('est_system_cost'), styles['BodyBold']), Paragraph(f"<b>€ {financials_data.get('total_cost', 0):,.2f}</b>", styles['Body'])], [Paragraph(get_text('total_annual_benefit'), styles['BodyBold']), Paragraph(f"€ {financials_data.get('total_annual_benefit', 0):,.2f}", styles['Body'])], [Paragraph(get_text('payback_period'), styles['BodyBold']), Paragraph(f"{financials_data.get('payback_period', 0):.1f} {get_text('years')}", styles['Body'])]], colWidths=[3 * inch, 3.5 * inch]))
    
    # --- Self-Consumption Analysis ---
    sc_data = session_data.get('final_sc')
    if sc_data:
        story.append(Paragraph(get_text('pdf_sc_title'), styles['H1']))
        story.append(Table([[Paragraph(get_text('pdf_sc_self_consumed'), styles['BodyBold']), Paragraph(f"{sc_data.get('self_consumed_kwh', 0):,.0f} kWh", styles['Body'])], [Paragraph(get_text('pdf_sc_exported'), styles['BodyBold']), Paragraph(f"{sc_data.get('grid_exported_kwh', 0):,.0f} kWh", styles['Body'])], [Paragraph(get_text('pdf_sc_savings'), styles['BodyBold']), Paragraph(f"€ {financials_data.get('annual_savings', 0):,.2f}", styles['Body'])], [Paragraph(get_text('pdf_sc_feed_in'), styles['BodyBold']), Paragraph(f"€ {financials_data.get('annual_feed_in', 0):,.2f}", styles['Body'])]], colWidths=[3 * inch, 3.5 * inch]))

    # --- CORRECTED & FULLY IMPLEMENTED Conditional Add-on Sections ---
    if session_data.get('report_include_addons'):
        if session_data.get('add_ev'):
            story.append(Paragraph(get_text('pdf_ev_details'), styles['H1']))
            # Recalculate base yield just for this context
            base_yield = sizing.calculate_energy_output(sizing.calculate_max_system_size(session_data.get('total_area',0), session_data.get('override_panel_density'))[0], session_data.get('pvgis_data')['total_yearly_kwh'])
            ev_reqs = ev.calculate_ev_requirements(session_data.get('num_evs', 1), session_data.get('daily_km', 50), base_yield)
            ev_table_data = [
                [Paragraph(get_text('pdf_num_evs'), styles['BodyBold']), Paragraph(str(session_data.get('num_evs', 'N/A')), styles['Body'])],
                [Paragraph(get_text('pdf_daily_km'), styles['BodyBold']), Paragraph(f"{session_data.get('daily_km', 'N/A')} km", styles['Body'])],
                [Paragraph(get_text('pdf_charger_type'), styles['BodyBold']), Paragraph(session_data.get('charger_type', 'N/A'), styles['Body'])],
                [Paragraph(get_text('pdf_ev_extra_kwp'), styles['BodyBold']), Paragraph(f"{ev_reqs['extra_kwp_needed']:.2f} kWp", styles['Body'])],
            ]
            story.append(Table(ev_table_data, colWidths=[3 * inch, 3.5 * inch]))

        if session_data.get('add_battery'):
            story.append(Paragraph(get_text('pdf_battery_details'), styles['H1']))
            battery_cost_val = battery.calculate_battery_cost(session_data.get('battery_kwh', 0), session_data.get('override_battery_cost'))
            battery_table_data = [
                [Paragraph(get_text('pdf_battery_size'), styles['BodyBold']), Paragraph(f"{session_data.get('battery_kwh', 0):.1f} kWh", styles['Body'])],
                [Paragraph(get_text('pdf_battery_cost'), styles['BodyBold']), Paragraph(f"€ {battery_cost_val:,.2f}", styles['Body'])],
            ]
            story.append(Table(battery_table_data, colWidths=[3 * inch, 3.5 * inch]))
            
    # --- Conditional Sustainability Section ---
    if session_data.get('report_include_sustainability'):
        story.append(Paragraph(get_text('pdf_sustainability_title'), styles['H1']))
        co2_saved_tonnes = (sizing_data.get('yield', 0) * 0.4) / 1000
        trees_equivalent = int(co2_saved_tonnes * 1000 / 21)
        story.append(Paragraph(f"By installing this solar system, you could offset approximately <b>{co2_saved_tonnes:.2f} tonnes of CO₂</b> annually, which is equivalent to the carbon sequestered by <b>{trees_equivalent} mature trees</b> each year.", styles['Body']))
    
    try:
        doc.build(story, onFirstPage=_add_footer, onLaterPages=_add_footer)
        return filename
    except Exception as e:
        print(f"Error building PDF: {e}")
        return None
