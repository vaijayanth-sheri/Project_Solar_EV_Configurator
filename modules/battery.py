# modules/battery.py

# Updated cost for battery storage as per new prompt
COST_PER_KWH_BATTERY = 700 # EUR or USD

def calculate_battery_cost(capacity_kwh):
    """Calculates the additional cost for a battery system."""
    return capacity_kwh * COST_PER_KWH_BATTERY