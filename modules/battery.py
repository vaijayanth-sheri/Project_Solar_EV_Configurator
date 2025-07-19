# solar_configurator/modules/battery.py

# Default cost for battery storage (CORRECTED to FLOAT)
DEFAULT_BATTERY_COST_PER_KWH = 700.0 # Was 700 (int) -> Now 700.0 (float)

def calculate_battery_cost(capacity_kwh: float, cost_per_kwh_override: float = None) -> float:
    """Calculates the additional cost for a battery system, using an override if provided."""
    cost_per_kwh = cost_per_kwh_override if cost_per_kwh_override is not None else DEFAULT_BATTERY_COST_PER_KWH
    return capacity_kwh * cost_per_kwh
