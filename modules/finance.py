# solar_configurator/modules/finance.py

# --- Default German Market Values ---
DEFAULT_SYSTEM_COST_PER_KWP = 1400.0
DEFAULT_ELECTRICITY_PRICE_SAVED = 0.29
DEFAULT_FEED_IN_TARIFF = 0.0794
DEFAULT_LIFETIME = 25.0

def calculate_financials(
    system_kwp: float, self_consumed_kwh: float, grid_exported_kwh: float, 
    battery_cost: float = 0, cost_per_kwp_override: float = None,
    electricity_price_override: float = None, feed_in_tariff_override: float = None,
    # System lifetime is passed for future use (e.g., LCOE) but doesn't affect simple payback
    lifetime_override: float = None 
) -> dict:
    """Calculates detailed financial performance, using override values if provided."""
    # Use override if provided, else use default
    system_cost_per_kwp = cost_per_kwp_override if cost_per_kwp_override is not None else DEFAULT_SYSTEM_COST_PER_KWP
    electricity_price_saved = electricity_price_override if electricity_price_override is not None else DEFAULT_ELECTRICITY_PRICE_SAVED
    feed_in_tariff = feed_in_tariff_override if feed_in_tariff_override is not None else DEFAULT_FEED_IN_TARIFF
    
    if system_kwp <= 0:
        return {'total_cost': 0, 'annual_savings': 0, 'annual_feed_in': 0, 'total_annual_benefit': 0, 'payback_period': float('inf')}

    pv_cost = system_kwp * system_cost_per_kwp
    total_investment = pv_cost + battery_cost

    annual_savings = self_consumed_kwh * electricity_price_saved
    annual_feed_in = grid_exported_kwh * feed_in_tariff
    total_annual_benefit = annual_savings + annual_feed_in
    
    payback_period = float('inf')
    if total_annual_benefit > 0:
        payback_period = total_investment / total_annual_benefit

    return {
        'total_cost': round(total_investment, 2),
        'annual_savings': round(annual_savings, 2),
        'annual_feed_in': round(annual_feed_in, 2),
        'total_annual_benefit': round(total_annual_benefit, 2),
        'payback_period': round(payback_period, 1)
    }
