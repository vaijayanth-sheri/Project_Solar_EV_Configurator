import math

# Constants
PANEL_WATTAGE = 410  # Wp per panel
PANEL_AREA = 1.8  # m² per panel (e.g., 1.7m x 1.05m)

def calculate_max_system_size(area_m2):
    """Calculates the maximum possible system size in kWp for a given area."""
    if area_m2 <= 0:
        return 0, 0
    
    num_panels = math.floor(area_m2 / PANEL_AREA)
    max_kwp = (num_panels * PANEL_WATTAGE) / 1000
    return round(max_kwp, 2), num_panels

def calculate_system_details(selected_kwp):
    """Calculates panel count and area for a given system size."""
    if selected_kwp <= 0:
        return 0, 0
    
    num_panels = math.ceil((selected_kwp * 1000) / PANEL_WATTAGE)
    required_area = num_panels * PANEL_AREA
    return num_panels, round(required_area, 2)

def calculate_energy_output(system_kwp, pvgis_yearly_kwh_per_kwp):
    """Calculates the total estimated yearly energy output."""
    return system_kwp * pvgis_yearly_kwh_per_kwp