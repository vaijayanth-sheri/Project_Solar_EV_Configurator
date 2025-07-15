# i18n/lang_dict.py
TEXT = {
    # ... (all previous keys are unchanged) ...
    'app_title': {'en': "Solar Configurator", 'de': "Solar Konfigurator"},
    'app_header': {'en': "Eco-Friendly Solar Planner", 'de': "Umweltfreundlicher Solarplaner"},
    'language': {'en': "Language", 'de': "Sprache"},
    'nav_location': {'en': "1. Location", 'de': "1. Standort"},
    'nav_rooftop': {'en': "2. Rooftop", 'de': "2. Dachfläche"},
    'nav_analysis': {'en': "3. Analysis & Add-ons", 'de': "3. Analyse & Extras"},
    'nav_report': {'en': "4. Report", 'de': "4. Bericht"},
    'calculate_button': {'en': "Calculate / Recalculate", 'de': "Berechnen / Neuberechnen"},

    # ... other keys ...
    'ev_charger_option': {'en': "Plan for EV Charging", 'de': "Für E-Fahrzeug-Laden planen"},
    'extra_kwp_needed': {'en': "Additional PV Size Needed", 'de': "Zusätzlich benötigte PV-Größe"},
    'ev_sufficient_msg': {'en': "Your base rooftop system is large enough to cover this EV demand.", 'de': "Ihre Basis-Dachanlage ist groß genug, um diesen E-Fahrzeug-Bedarf zu decken."},
    
    # --- About Section Text ---
    'about_header': {'en': "About this tool", 'de': "Über dieses Tool"},
    'about_overview_title': {'en': "Tool Overview", 'de': "Werkzeugübersicht"},
    'about_overview_text': {
        'en': "This tool is a solar energy system configurator that helps users quickly estimate the feasibility of installing rooftop solar panels based on their location and selected area. It also optionally includes EV charging and battery planning for integrated smart energy solutions.",
        'de': "Dieses Tool ist ein Konfigurator für Solarenergiesysteme, der Benutzern hilft, die Machbarkeit der Installation von Aufdach-Solaranlagen basierend auf ihrem Standort und der ausgewählten Fläche schnell abzuschätzen. Optional beinhaltet es auch die Planung von E-Fahrzeug-Ladestationen und Batteriespeichern für integrierte intelligente Energielösungen."
    },
    'about_tech_title': {'en': "Technical Details & Assumptions", 'de': "Technische Details & Annahmen"},
    'about_tech_text': {
        'en': """
        *   **Solar Irradiance:** Data is fetched via the **PVGIS API** based on user coordinates.
        *   **System Sizing:** Assumes a standard module density of approx. **6.5 m² per kWp**.
        *   **Performance Ratio (PR):** Defaults to **0.75**, which accounts for losses (shading, orientation, etc.).
        *   **Financials:** Based on average costs of **€1200/kWp** for PV and electricity savings of **€0.30/kWh**.
        *   **EV Needs:** Calculated using **0.17 kWh/km** average consumption.
        *   **Battery Costs:** Assumes **€700/kWh** for installation.
        """,
        'de': """
        *   **Sonneneinstrahlung:** Daten werden über die **PVGIS-API** basierend auf den Benutzerkoordinaten abgerufen.
        *   **Systemgröße:** Geht von einer Standard-Moduldichte von ca. **6,5 m² pro kWp** aus.
        *   **Performance Ratio (PR):** Standardmäßig **0,75**, was Verluste (Verschattung, Ausrichtung etc.) berücksichtigt.
        *   **Finanzen:** Basierend auf Durchschnittskosten von **1200 €/kWp** für PV und Stromersparnissen von **0,30 €/kWh**.
        *   **E-Fahrzeug-Bedarf:** Berechnet mit einem Durchschnittsverbrauch von **0,17 kWh/km**.
        *   **Batteriekosten:** Geht von **700 €/kWh** für die Installation aus.
        """
    },
    'about_limits_title': {'en': "Results & Limitations", 'de': "Ergebnisse & Einschränkungen"},
    'about_limits_text': {
        'en': "The outputs are **preliminary planning estimates** and should not replace a professional on-site assessment. Final system performance will vary based on installation quality, regional pricing, and grid policies.",
        'de': "Die Ergebnisse sind **vorläufige Planungsschätzungen** und sollten eine professionelle Bewertung vor Ort nicht ersetzen. Die endgültige Systemleistung hängt von der Installationsqualität, regionalen Preisen und Netzrichtlinien ab."
    },
    'about_future_title': {'en': "Future Features (Planned)", 'de': "Zukünftige Funktionen (Geplant)"},
    'about_future_text': {
        'en': """
        *   Roof orientation and tilt configuration
        *   Dynamic battery discharge simulations
        *   Detailed CO₂ savings calculation
        *   Support for feed-in tariffs or net-metering
        """,
        'de': """
        *   Konfiguration von Dachaausrichtung und -neigung
        *   Dynamische Simulationen der Batterieentladung
        *   Detaillierte Berechnung der CO₂-Einsparungen
        *   Unterstützung für Einspeisevergütungen oder Net-Metering
        """
    }
}
# Add the rest of the original TEXT dictionary here
TEXT.update({
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
    'base_system_header': {'en': "Base System (from Roof Area)", 'de': "Basissystem (aus Dachfläche)"},
    'total_system_header': {'en': "Total Combined System", 'de': "Gesamtes kombiniertes System"},
    'sizing_subheader': {'en': "System Sizing & Performance", 'de': "Systemgröße & Leistung"},
    'est_yearly_output': {'en': "Estimated Yearly Output", 'de': "Geschätzte Jahresproduktion"},
    'total_system_size': {'en': "Total System Size (Roof + EV)", 'de': "Gesamte Systemgröße (Dach + EV)"},
    'total_yearly_yield': {'en': "Total Yearly Yield", 'de': "Gesamter Jahresertrag"},
    'financial_subheader': {'en': "Financial Summary", 'de': "Finanzielle Zusammenfassung"},
    'est_system_cost': {'en': "Estimated System Cost (PV + Battery)", 'de': "Geschätzte Systemkosten (PV + Batterie)"},
    'est_yearly_savings': {'en': "Estimated Yearly Savings", 'de': "Geschätzte jährliche Ersparnis"},
    'payback_period': {'en': "Simple Payback Period", 'de': "Einfache Amortisationszeit"},
    'years': {'en': "years", 'de': "Jahre"},
    'addons_header': {'en': "Optional Add-ons", 'de': "Optionale Extras"},
    'num_evs': {'en': "Number of Electric Vehicles", 'de': "Anzahl der Elektrofahrzeuge"},
    'daily_driving_distance': {'en': "Avg. daily driving distance per EV (km)", 'de': "Ø tägliche Fahrstrecke pro E-Fahrzeug (km)"},
    'charger_type': {'en': "Charger Type", 'de': "Ladegerät-Typ"},
    'ev_upsizing_header': {'en': "EV Upsizing Requirements", 'de': "Anforderungen zur EV-Erweiterung"},
    'ev_energy_needs': {'en': "Total daily energy for EVs", 'de': "Gesamter täglicher Energiebedarf für E-Fahrzeuge"},
    'battery_option': {'en': "Add Battery Storage", 'de': "Batteriespeicher hinzufügen"},
    'battery_capacity': {'en': "Select Battery Capacity (kWh)", 'de': "Batteriekapazität auswählen (kWh)"},
    'additional_cost': {'en': "Additional Cost for Battery", 'de': "Zusätzliche Kosten für Batterie"},
    'report_header': {'en': "Download Your Report", 'de': "Laden Sie Ihren Bericht herunter"},
    'generate_report_button': {'en': "Generate PDF Report", 'de': "PDF-Bericht erstellen"},
    'download_report_button': {'en': "Download PDF", 'de': "PDF herunterladen"},
    'pdf_title': {'en': "Solar Potential Report", 'de': "Solarpotenzial-Bericht"},
    'pdf_system_size': {'en': "System Size", 'de': "Anlagengröße"},
    'panel_count': {'en': "Panel Count", 'de': "Modulanzahl"},
    'warning_need_location': {'en': "Please complete Step 1: Location first.", 'de': "Bitte zuerst Schritt 1: Standort ausfüllen."},
    'warning_need_rooftop': {'en': "Please complete Step 2: Rooftop by drawing a valid area on the map.", 'de': "Bitte zuerst Schritt 2: Dachfläche durch Einzeichnen eines gültigen Bereichs auf der Karte abschließen."},
    'warning_analysis_incomplete': {'en': "Please complete the analysis on the 'Analysis & Add-ons' page first.", 'de': "Bitte zuerst die Analyse auf der Seite 'Analyse & Extras' durchführen."},
    'info_click_calculate': {'en': "Adjust add-ons and click 'Calculate / Recalculate' to see the final results.", 'de': "Passen Sie die Extras an und klicken Sie auf 'Berechnen / Neuberechnen', um die Endergebnisse zu sehen."},
    'error_pvgis_fail': {'en': "Failed to fetch PVGIS data. Please try again.", 'de': "Abrufen der PVGIS-Daten fehlgeschlagen. Bitte versuchen Sie es erneut."},
    'error_pdf_fail': {'en': "Failed to generate PDF report.", 'de': "PDF-Bericht konnte nicht erstellt werden."}
})