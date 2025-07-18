# solar_configurator/i18n/lang_dict.py

TEXT = {
    'app_title': {'en': "Solar Configurator", 'de': "Solar Konfigurator"},
    'app_header': {'en': "Eco-Friendly Solar Planner", 'de': "Umweltfreundlicher Solarplaner"},
    'language': {'en': "Language", 'de': "Sprache"},
    'nav_location': {'en': "1. Location", 'de': "1. Standort"},
    'nav_rooftop': {'en': "2. Rooftop", 'de': "2. Dachfläche"},
    'nav_analysis': {'en': "3. Analysis & Add-ons", 'de': "3. Analyse & Extras"},
    'nav_report': {'en': "4. Report", 'de': "4. Bericht"},
    'location_header': {'en': "Enter Your Address", 'de': "Geben Sie Ihre Adresse ein"},
    'address_input_label': {'en': "e.g., 1600 Amphitheatre Parkway, Mountain View, CA", 'de': "z.B., Willy-Brandt-Straße 1, 10557 Berlin"},
    'geocode_button': {'en': "Find Location", 'de': "Standort finden"},
    'geocode_success': {'en': "Location found!", 'de': "Standort gefunden!"},
    'geocode_error': {'en': "Could not find address. Please try again.", 'de': "Adresse nicht gefunden. Bitte versuchen Sie es erneut."},
    'rooftop_header': {'en': "Draw Your Rooftop Area(s)", 'de': "Zeichnen Sie Ihre Dachfläche(n) ein"},
    'rooftop_instruction': {'en': "Use the polygon tool on the map to outline the usable areas of your roof. You can draw multiple polygons.", 'de': "Verwenden Sie das Polygon-Werkzeug auf der Karte, um die nutzbaren Bereiche Ihres Daches zu markieren. Sie können mehrere Polygone zeichnen."},
    'total_roof_area': {'en': "Total Roof Area", 'de': "Gesamtdachfläche"},
    'analysis_header': {'en': "System Analysis", 'de': "Systemanalyse"},
    'total_system_header': {'en': "Total Combined System", 'de': "Gesamtes kombiniertes System"},
    'sizing_subheader': {'en': "System Sizing & Performance", 'de': "Systemgröße & Leistung"},
    'total_system_size': {'en': "Total System Size (Roof + EV)", 'de': "Gesamte Systemgröße (Dach + EV)"},
    'total_yearly_yield': {'en': "Total Yearly Yield (Year 1)", 'de': "Gesamter Jahresertrag (Jahr 1)"},
    'financial_subheader': {'en': "Financial Summary", 'de': "Finanzielle Zusammenfassung"},
    'est_system_cost': {'en': "Estimated System Cost (PV + Battery)", 'de': "Geschätzte Systemkosten (PV + Batterie)"},
    'payback_period': {'en': "Simple Payback Period", 'de': "Einfache Amortisationszeit"},
    'years': {'en': "years", 'de': "Jahre"},
    'addons_header': {'en': "Optional Add-ons", 'de': "Optionale Extras"},
    'ev_charger_option': {'en': "Plan for EV Charging", 'de': "Für E-Fahrzeug-Laden planen"},
    'ev_sufficient_msg': {'en': "Your base rooftop system is large enough to cover this EV demand.", 'de': "Ihre Basis-Dachanlage ist groß genug, um diesen E-Fahrzeug-Bedarf zu decken."},
    'battery_option': {'en': "Add Battery Storage", 'de': "Batteriespeicher hinzufügen"},
    'report_header': {'en': "Download Your Report", 'de': "Laden Sie Ihren Bericht herunter"},
    'generate_report_button': {'en': "Generate PDF Report", 'de': "PDF-Bericht erstellen"},
    'download_report_button': {'en': "Download PDF", 'de': "PDF herunterladen"},
    'about_header': {'en': "Expert Settings", 'de': "Experteneinstellungen"},
    'about_tech_title': {'en': "Expert Settings & Assumptions", 'de': "Experteneinstellungen & Annahmen"},
    'about_tech_text': {'en': "Override default values to match your specific market conditions. Changes apply for this session only.", 'de': "Überschreiben Sie die Standardwerte, um sie an Ihre Marktbedingungen anzupassen. Änderungen gelten nur für diese Sitzung."},
    'about_form_save_button': {'en': "Apply Custom Settings", 'de': "Einstellungen anwenden"},
    'about_form_success': {'en': "Custom settings applied for this session!", 'de': "Benutzerdefinierte Einstellungen für diese Sitzung angewendet!"},
    'cat_location': {'en': "1. Location & Rooftop", 'de': "1. Standort & Dach"},
    'cat_irradiance': {'en': "2. Irradiance & Climate", 'de': "2. Einstrahlung & Klima"},
    'cat_system': {'en': "3. System Components", 'de': "3. Systemkomponenten"},
    'cat_self_consumption': {'en': "4. Self-Consumption & Load", 'de': "4. Eigenverbrauch & Lastprofil"},
    'cat_ev': {'en': "5. EV Charging Profile", 'de': "5. E-Fahrzeug-Ladeprofil"},
    'cat_battery': {'en': "6. Battery Storage", 'de': "6. Batteriespeicher"},
    'cat_financial': {'en': "7. Financial Parameters", 'de': "7. Finanzparameter"},
    'cat_report': {'en': "8. Report Customization", 'de': "8. Berichtsanpassung"},
    'form_orientation': {'en': "Orientation / Azimuth (°)", 'de': "Ausrichtung / Azimut (°)"},
    'form_tilt': {'en': "Tilt Angle (°)", 'de': "Neigungswinkel (°)"},
    'form_degradation': {'en': "Degradation Rate (%/year)", 'de': "Degradationsrate (%/Jahr)"},
    'form_losses': {'en': "Total System Losses (%)", 'de': "Gesamte Systemverluste (%)"},
    'form_panel_density': {'en': "Panel Density (m²/kWp)", 'de': "Modulflächendichte (m²/kWp)"},
    'form_system_lifetime': {'en': "System Lifetime (years)", 'de': "Systemlebensdauer (Jahre)"},
    'form_placeholder_soon': {'en': "For future simulation", 'de': "Für zukünftige Simulation"},
    'report_include_addons': {'en': "Include EV/Battery sections in report", 'de': "EV/Batterie-Abschnitte in Bericht aufnehmen"},
    'report_include_sustainability': {'en': "Include Sustainability section in report", 'de': "Nachhaltigkeits-Abschnitt in Bericht aufnehmen"},
    'sc_header': {'en': "Self-Consumption Settings", 'de': "Eigenverbrauchseinstellungen"},
    'sc_input_mode': {'en': "Calculation Mode", 'de': "Berechnungsmodus"},
    'sc_mode_annual_kwh': {'en': "Annual Consumption (kWh)", 'de': "Jahresverbrauch (kWh)"},
    'sc_mode_percentage': {'en': "Self-Consumption (%)", 'de': "Eigenverbrauch (%)"},
    'sc_annual_label': {'en': "Your annual electricity consumption (kWh/year)", 'de': "Ihr jährlicher Stromverbrauch (kWh/Jahr)"},
    'sc_percentage_label': {'en': "Percentage of solar energy you consume on-site", 'de': "Prozentsatz der Solarenergie, den Sie vor Ort verbrauchen"},
    'total_annual_benefit': {'en': "Total Annual Benefit", 'de': "Gesamter jährlicher Nutzen"},
    'warning_need_location': {'en': "Please complete Step 1: Location first.", 'de': "Bitte zuerst Schritt 1: Standort ausfüllen."},
    'warning_need_rooftop': {'en': "Please complete Step 2: Rooftop by drawing a valid area on the map.", 'de': "Bitte zuerst Schritt 2: Dachfläche durch Einzeichnen eines gültigen Bereichs auf der Karte abschließen."},
    'warning_analysis_incomplete': {'en': "Please complete the analysis on the 'Analysis & Add-ons' page first.", 'de': "Bitte zuerst die Analyse auf der Seite 'Analyse & Extras' durchführen."},
    'error_pvgis_fail': {'en': "Failed to fetch PVGIS data. Please try again.", 'de': "Abrufen der PVGIS-Daten fehlgeschlagen. Bitte versuchen Sie es erneut."},
    'error_pdf_fail': {'en': "Failed to generate PDF report.", 'de': "PDF-Bericht konnte nicht erstellt werden."},

    # --- Report Specific Keys ---
    'pdf_title': {'en': "Solar Potential Report", 'de': "Solarpotenzial-Bericht"},
    'pdf_expert_settings_summary': {'en': "Expert Settings Summary", 'de': "Zusammenfassung der Experteneinstellungen"},
    'pdf_custom_value_info': {'en': "This report was generated using the following custom parameters.", 'de': "Dieser Bericht wurde mit den folgenden benutzerdefinierten Parametern erstellt."},
    'pdf_default': {'en': "(Default)", 'de': "(Standard)"},
    'pdf_custom': {'en': "(Custom)", 'de': "(Benutzerdef.)"},
    'pdf_spec_title': {'en': "System Specification", 'de': "Systemspezifikation"},
    'pdf_usable_area': {'en': "Total Usable Area", 'de': "Gesamte Nutzfläche"},
    'pdf_panel_count': {'en': "Estimated Panel Count", 'de': "Geschätzte Modulanzahl"},
    'pdf_yield_year_1': {'en': "Est. Annual Yield (Year 1)", 'de': "Gesch. Jahresertrag (Jahr 1)"},
    'pdf_sc_title': {'en': "Self-Consumption Analysis", 'de': "Eigenverbrauchsanalyse"},
    'pdf_sc_self_consumed': {'en': "Energy Used On-Site", 'de': "Energie vor Ort genutzt"},
    'pdf_sc_exported': {'en': "Energy Exported to Grid", 'de': "Energie ins Netz eingespeist"},
    'pdf_sc_savings': {'en': "Savings from Self-Consumption", 'de': "Ersparnis durch Eigenverbrauch"},
    'pdf_sc_feed_in': {'en': "Revenue from Feed-in Tariff", 'de': "Einnahmen durch Einspeisevergütung"},
    'pdf_ev_details': {'en': "EV Charging Details", 'de': "Details zum E-Fahrzeug-Laden"},
    'pdf_num_evs': {'en': "Number of EVs", 'de': "Anzahl der E-Fahrzeuge"},
    'pdf_daily_km': {'en': "Daily Distance per EV", 'de': "Tägliche Strecke pro E-Fahrzeug"},
    'pdf_charger_type': {'en': "Recommended Charger", 'de': "Empfohlenes Ladegerät"},
    'pdf_ev_extra_kwp': {'en': "PV Upsize for EVs", 'de': "PV-Erweiterung für E-Fahrzeuge"},
    'pdf_battery_details': {'en': "Battery Storage Details", 'de': "Details zum Batteriespeicher"},
    'pdf_battery_size': {'en': "Battery Size", 'de': "Batteriegröße"},
    'pdf_battery_cost': {'en': "Estimated Battery Cost", 'de': "Geschätzte Batteriekosten"},
    'pdf_sustainability_title': {'en': "Sustainability Highlights", 'de': "Nachhaltigkeits-Highlights"},
}
