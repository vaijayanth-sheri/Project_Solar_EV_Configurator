# solar_configurator/modules/self_consumption.py

def calculate_self_consumption(
    pv_yield_kwh: float, 
    mode: str, 
    annual_consumption_kwh: int, 
    self_consumption_pct: int
) -> dict:
    """
    Calculates the amount of solar energy consumed on-site vs. exported to the grid.

    Args:
        pv_yield_kwh: Total annual energy produced by the solar system.
        mode: The calculation mode ('annual_kwh' or 'percentage').
        annual_consumption_kwh: The user's total annual electricity consumption.
        self_consumption_pct: The percentage of solar energy consumed on-site.

    Returns:
        A dictionary containing the breakdown of energy usage.
    """
    self_consumed_kwh = 0
    grid_exported_kwh = 0

    if mode == 'annual_kwh' and annual_consumption_kwh > 0:
        # Self-consumed energy cannot exceed production or consumption.
        self_consumed_kwh = min(float(annual_consumption_kwh), pv_yield_kwh)
        grid_exported_kwh = pv_yield_kwh - self_consumed_kwh
    elif mode == 'percentage' and self_consumption_pct > 0:
        # Calculate based on a direct percentage of the yield.
        self_consumed_kwh = pv_yield_kwh * (self_consumption_pct / 100.0)
        grid_exported_kwh = pv_yield_kwh - self_consumed_kwh
    else:
        # Default/fallback: A simple model where 30% is self-consumed if no valid input.
        # This provides a reasonable starting point.
        self_consumed_kwh = pv_yield_kwh * 0.30
        grid_exported_kwh = pv_yield_kwh - self_consumed_kwh

    return {
        "self_consumed_kwh": round(self_consumed_kwh, 2),
        "grid_exported_kwh": round(grid_exported_kwh, 2),
        "mode": mode,
        "input_value_kwh": annual_consumption_kwh,
        "input_value_pct": self_consumption_pct
    }