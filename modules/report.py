import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.lib import colors

# --- THEME & STYLING ---
primary_color = colors.HexColor('#2E7D32')  # Soft Green
secondary_color = colors.HexColor('#1E88E5') # Blue Accent
text_color = colors.HexColor('#37474F')
light_grey = colors.lightgrey

def _add_footer(canvas, doc):
    """Adds a footer to each page."""
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawString(inch, 0.75 * inch, f"Page {doc.page} | Solar Configurator Report")
    canvas.restoreState()

def generate(polygons: list, sizing: dict, financials: dict, location: dict, pvgis: dict, ev: dict or None, battery: dict or None, text: dict, lang: str) -> str or None:
    """
    Generates a detailed, styled PDF report from solar configuration data.
    """
    filename = "output/solar_report.pdf"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # --- STYLES ---
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CoverTitle', fontName='Helvetica-Bold', fontSize=28, alignment=TA_CENTER, textColor=primary_color, spaceAfter=20))
    styles.add(ParagraphStyle(name='H1', fontName='Helvetica-Bold', fontSize=18, alignment=TA_LEFT, textColor=primary_color, spaceBefore=20, spaceAfter=10, borderPadding=5))
    styles.add(ParagraphStyle(name='H2', fontName='Helvetica-Bold', fontSize=14, alignment=TA_LEFT, textColor=text_color, spaceBefore=10, spaceAfter=5))
    styles.add(ParagraphStyle(name='Body', fontName='Helvetica', fontSize=11, alignment=TA_LEFT, textColor=text_color, leading=14))
    styles.add(ParagraphStyle(name='Small', fontName='Helvetica', fontSize=9, alignment=TA_LEFT, textColor=colors.grey, leading=12))

    def get_text(key):
        return text.get(key, {}).get(lang, key.replace('_', ' ').title())

    story = []

    # --- 1. COVER PAGE ---
    story.append(Paragraph(get_text('pdf_title'), styles['CoverTitle']))
    story.append(Spacer(1, 2 * inch))
    summary_data = [
        [Paragraph('<b>Location</b>', styles['Body']), Paragraph(location.get('address', 'N/A'), styles['Body'])],
        [Paragraph('<b>Report Date</b>', styles['Body']), Paragraph(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), styles['Body'])],
        [Paragraph('<b>System Size</b>', styles['Body']), f"{sizing.get('kwp', 0):.2f} kWp"],
        [Paragraph('<b>Est. Annual Yield</b>', styles['Body']), f"{sizing.get('yield', 0):,.0f} kWh"],
    ]
    summary_table = Table(summary_data, colWidths=[2 * inch, 4.5 * inch])
    summary_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(summary_table)
    story.append(PageBreak())

    # --- 2. ROOFTOP & 3. IRRADIANCE ---
    story.append(Paragraph(get_text('pdf_rooftop'), styles['H1']))
    rooftop_data = [
        [Paragraph('<b>Number of Marked Areas</b>', styles['Body']), len(polygons)],
        [Paragraph(f"<b>{get_text('total_roof_area')}</b>", styles['Body']), f"{sizing.get('area', 0):.2f} m²"],
    ]
    story.append(Table(rooftop_data, colWidths=[3 * inch, 3.5 * inch]))

    story.append(Paragraph("Solar Irradiance Summary", styles['H2']))
    irradiance_data = [
        ['Data Source:', 'PVGIS © European Union'],
        ['Avg. Daily Production (per kWp):', f"{pvgis.get('avg_daily_kwh', 0):.2f} kWh"],
        ['Avg. Yearly Production (per kWp):', f"{pvgis.get('total_yearly_kwh', 0):.0f} kWh"],
    ]
    story.append(Table(irradiance_data, colWidths=[3 * inch, 3.5 * inch]))
    
    # --- 4. SYSTEM SIZING ---
    story.append(Paragraph(get_text('sizing_subheader'), styles['H1']))
    sizing_data = [
        [get_text('total_system_size'), f"<b>{sizing.get('kwp', 0):.2f} kWp</b>"],
        [get_text('panel_count'), f"~ {sizing.get('panels', 0)}"],
        [get_text('total_yearly_yield'), f"<b>{sizing.get('yield', 0):,.0f} kWh/year</b>"],
    ]
    sizing_table = Table([[Paragraph(cell, styles['Body']) for cell in row] for row in sizing_data], colWidths=[3 * inch, 3.5 * inch])
    story.append(sizing_table)
    story.append(Paragraph("<i>Assumptions: Standard panel efficiency, 14% system loss (derating). Actuals may vary.</i>", styles['Small']))

    # --- 5. FINANCIAL SUMMARY ---
    story.append(Paragraph(get_text('financial_subheader'), styles['H1']))
    try:
        roi = (financials.get('savings', 0) / financials.get('cost', 1)) * 100
    except ZeroDivisionError:
        roi = 0
    financial_data = [
        [get_text('est_system_cost'), f"<b>€ {financials.get('cost', 0):,.2f}</b>"],
        [get_text('est_yearly_savings'), f"€ {financials.get('savings', 0):,.2f}"],
        [get_text('payback_period'), f"{financials.get('payback', 0):.1f} {get_text('years')}"],
        ["Simple Return on Investment (ROI)", f"{roi:.1f}% per year"],
    ]
    financial_table = Table([[Paragraph(cell, styles['Body']) for cell in row] for row in financial_data], colWidths=[3 * inch, 3.5 * inch])
    story.append(financial_table)
    
    # --- 6. EV CHARGING DETAILS (Conditional) ---
    if ev:
        story.append(Paragraph(get_text('ev_charger_option'), styles['H1']))
        ev_data = [
            [get_text('num_evs'), ev.get('count', 'N/A')],
            [get_text('daily_driving_distance'), f"{ev.get('daily_km', 'N/A')} km"],
            [get_text('charger_type'), ev.get('charger', 'N/A')],
            [get_text('ev_energy_needs'), f"{ev.get('kwh_daily', 0):.2f} kWh"],
            [get_text('extra_kwp_needed'), f"{ev.get('extra_kwp', 0):.2f} kWp"],
        ]
        ev_table = Table([[Paragraph(str(cell), styles['Body']) for cell in row] for row in ev_data], colWidths=[3 * inch, 3.5 * inch])
        story.append(ev_table)

    # --- 7. BATTERY STORAGE DETAILS (Conditional) ---
    if battery:
        story.append(Paragraph(get_text('battery_option'), styles['H1']))
        battery_data = [
            [get_text('battery_capacity'), f"{battery.get('size', 0)} kWh"],
            [get_text('additional_cost'), f"€ {battery.get('cost', 0):,.2f}"],
        ]
        battery_table = Table([[Paragraph(str(cell), styles['Body']) for cell in row] for row in battery_data], colWidths=[3 * inch, 3.5 * inch])
        story.append(battery_table)
        story.append(Paragraph("<i>Note: This is a cost estimate. A detailed dispatch simulation is not included.</i>", styles['Small']))

    # --- 8. SUSTAINABILITY HIGHLIGHTS ---
    story.append(Paragraph("Sustainability Highlights", styles['H1']))
    co2_saved_tonnes = (sizing.get('yield', 0) * 0.4) / 1000 # Using a more conservative 0.4 kg/kWh
    trees_equivalent = int(co2_saved_tonnes * 1000 / 21) # Approx. 21 kg CO2/year per tree
    
    sustainability_text = f"""
    By installing this solar system, you are making a significant positive impact on the environment.
    <ul>
        <li>You could offset approximately <b>{co2_saved_tonnes:.2f} tonnes of CO₂</b> annually.</li>
        <li>This is equivalent to the carbon sequestered by <b>{trees_equivalent} mature trees</b> each year.</li>
    </ul>
    Embracing solar energy and clean mobility is a powerful step towards a sustainable future.
    """
    story.append(Paragraph(sustainability_text, styles['Body']))
    
    try:
        doc.build(story, onFirstPage=_add_footer, onLaterPages=_add_footer)
        return filename
    except Exception as e:
        print(f"Error building PDF: {e}")
        return None