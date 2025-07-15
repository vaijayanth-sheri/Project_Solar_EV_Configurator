# Project_Solar_EV_Configurator
An interactive web app built with Python and Streamlit to visually plan and analyze rooftop solar systems with integrated EV and battery storage options.

# ☀️ Solar + EV Configurator

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web-based tool built with Python and Streamlit to help homeowners and consultants plan and analyze rooftop solar installations, with integrated support for EV charging and battery storage planning.

---

### Demo

Live Demo Link:    https://projectsolarevconfigurator.streamlit.app/ 

---
### 💡 Key Features

*   **📍 Interactive Location Selection:** Find any address on an interactive satellite map.
*   **✏️ Manual Rooftop Drawing:** Precisely draw one or more usable rooftop areas for accurate area calculation.
*   **☀️ Automated Solar Data:** Instantly fetches location-specific solar irradiance data from the PVGIS API.
*   **💡 Optimal System Sizing:** Get immediate estimates for system size (kWp) and panel count based on your drawn area.
*   **💰 Financial Analysis:** Understand your investment with clear metrics on total cost, annual savings, and payback period.
*   **🚗⚡ Integrated Add-ons:** Optionally model the impact of adding battery storage or planning for one or more EV chargers.
*   **📄 PDF Export:** Generate a clean, detailed report of your complete configuration for sharing and planning.
*   **🌍 Bilingual Support:** Fully functional in both English and German.

### 🛠️ Tech Stack

*   **Core Framework:** Python & Streamlit
*   **Geospatial & Mapping:** Geopy, Folium, streamlit-folium, Shapely, Pyproj
*   **Data & Simulation:** Pandas, Requests (for PVGIS API)
*   **PDF Reporting:** ReportLab
*   **UI Components:** streamlit-option-menu

### 📁 Project Structure

The project uses a clean, modular architecture to separate concerns:

```
solar_configurator/
│
├── app.py                      # Main Streamlit file
├── requirements.txt
├── .gitignore
├── README.md
│
├── modules/                    # Core logic modules
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
    git clone https://https://github.com/vaijayanth-sheri/Project_Solar_EV_Configurator.git
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

The application should now be open in your web browser!

### 🤝 Contributing

Feedback, bug reports, and pull requests are welcome! Feel free to open an issue to discuss a new feature or improvement.
