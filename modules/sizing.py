# solar_configurator/modules/sizing.py
import math

# Default Constants that can be overridden
DEFAULT_PANEL_WATTAGE = 410.0
DEFAULT_PANEL_DENSITY_KWP_PER_M2 = 1 / 6.5 # Corresponds to ~6.5 m²/kWp
DEFAULT_DEGRADATION_RATE = 0.005 # 0.5% per year

def calculate_max_system_size(
    area_m2: float, 
    panel_density_override: float = None
) -> tuple:
    """Calculates the maximum possible system size in kWp based on area and panel density."""
    # Use override if provided, else use default
    panel_density = panel_density_override if panel_density_override is not None else DEFAULT_PANEL_DENSITY_KWP_PER_M2
    
    if area_m2 <= 0 or panel_density <= 0:
        return 0, 0
    
    max_kwp = area_m2 * panel_density
    num_panels = math.ceil((max_kwp * 1000) / DEFAULT_PANEL_WATTAGE)
    return round(max_kwp, 2), num_panels

def calculate_system_details(selected_kwp: float) -> tuple:
    """Calculates panel count for a given system size."""
    if selected_kwp <= 0:
        return 0, 0
    
    num_panels = math.ceil((selected_kwp * 1000) / DEFAULT_PANEL_WATTAGE)
    return num_panels, None # Area calculation is now implicitly handled by density

def calculate_energy_output(
    system_kwp: float, 
    pvgis_yearly_kwh_per_kwp: float,
    degradation_rate_override: float = None
) -> float:
    """Calculates the Year 1 energy output, applying degradation."""
    # Use override if provided, else use default
    degradation_rate = degradation_rate_override if degradation_rate_override is not None else DEFAULT_DEGRADATION_RATE
    
    # Apply degradation for the first year's performance
    year_1_yield = system_kwp * pvgis_yearly_kwh_per_kwp * (1 - degradation_rate)
    return year_1_yield
