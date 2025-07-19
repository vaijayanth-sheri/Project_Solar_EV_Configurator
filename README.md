# Project_Solar_EV_Configurator
An interactive web app built with Python and Streamlit to visually plan and analyze rooftop solar systems with integrated EV and battery storage options.

# ☀️ Solar + EV Configurator

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced, web-based tool built with Python and Streamlit to help homeowners and energy consultants plan, analyze, and customize rooftop solar installations. It features integrated support for EV charging, battery storage, and a detailed self-consumption model with market-accurate financial calculations.

---

### 🚀 Live Demo

**Experience the tool live:** **[https://projectsolarevconfigurator.streamlit.app/](https://projectsolarevconfigurator.streamlit.app/)**



![Solar Configurator Demo](placeholder_for_demo.gif)

---

### 💡 Key Features

The application provides a seamless workflow from initial location selection to a detailed, exportable report.

#### Core Functionality:
*   **📍 Interactive Location Selection:** Find any address globally on a high-resolution satellite map.
*   **✏️ Manual Rooftop Drawing:** Precisely draw one or more usable rooftop areas for accurate area calculation.
*   **☀️ Automated Solar Data:** Instantly fetches location-specific solar irradiance data from the PVGIS API with automatic database switching for worldwide coverage.
*   **📊 Self-Consumption Modeling:** Simulate realistic financial outcomes based on either annual household electricity consumption (kWh) or a direct self-consumption percentage.
*   **💰 Detailed Financial Analysis:** Understand your investment with metrics on total cost, annual savings from self-use, feed-in tariff revenue, and a dynamic payback period based on market-accurate values.
*   **🚗⚡ Integrated Add-ons:** Model the impact of adding battery storage or planning for EV chargers, with intelligent system upsizing recommendations.
*   **📄 Professional PDF Export:** Generate a clean, detailed, and customizable report of your complete configuration, including all expert settings and financial breakdowns.
*   **🌍 Bilingual Support:** Fully functional in both English and German.

#### 🔧 Expert Settings Panel
For professionals and advanced users, the "Expert Settings" panel unlocks deep customization of the simulation:
*   **Rooftop Configuration:** Override default tilt and azimuth/orientation.
*   **Climate & Performance:** Adjust system losses and annual panel degradation rates.
*   **Financial Parameters:** Input custom values for system cost per kWp, battery cost per kWh, grid electricity price, and feed-in tariffs to match local market conditions.
*   **Report Customization:** Choose which optional sections (EV, Battery, Sustainability) to include in the final PDF report.

### 🛠️ Tech Stack

*   **Core Framework:** Python & Streamlit
*   **Geospatial & Mapping:** Geopy, Folium, streamlit-folium, Shapely, Pyproj
*   **Data & Simulation:** Pandas, Requests (for PVGIS API)
*   **PDF Reporting:** ReportLab
*   **UI Components:** streamlit-option-menu

### 📁 Updated Project Structure

The project uses a clean, modular architecture to separate concerns, making it scalable and easy to maintain.

```
solar_configurator/
│
├── app.py                      # Main Streamlit file
├── requirements.txt
├── .gitignore
├── README.md
│
├── modules/                    # Core logic modules
│   ├── self_consumption.py     # New
│   ├── location.py
│   ├── map_draw.py
│   ├── irradiance.py
│   ├── sizing.py
│   ├── finance.py
│   ├── ev.py
│   ├── battery.py
│   └── report.py
│
├── assets/
│   └── styles.css
│
├── i18n/
│   └── lang_dict.py            # English/German text
│
└── output/                     # (Ignored by Git)
```

---

### 🚀 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vaijayanth-sheri/Project_Solar_EV_Configurator.git
    cd Project_Solar_EV_Configurator
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

The application should now be open and running in your web browser!

### 🤝 Contributing

Feedback, bug reports, and pull requests are welcome! If you have ideas for new features (like advanced battery dispatch modeling or different financial incentives), please feel free to open an issue to start a discussion.
