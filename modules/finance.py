# modules/finance.py

# Constants for financial calculations
COST_PER_KWP_PV = 1200      # e.g., in EUR or USD for the PV system
ELECTRICITY_PRICE = 0.30  # e.g., EUR/kWh or USD/kWh

def calculate_financials(system_kwp, yearly_energy_kwh, battery_cost=0):
    """
    Calculates cost, savings, and payback period.
    Crucially, battery_cost is added to the total investment.
    """
    if system_kwp <= 0 or yearly_energy_kwh <= 0:
        return {
            'total_cost': 0,
            'yearly_savings': 0,
            'payback_period': float('inf')
        }

    pv_cost = system_kwp * COST_PER_KWP_PV
    total_investment = pv_cost + battery_cost  # This sum is critical
    
    yearly_savings = yearly_energy_kwh * ELECTRICITY_PRICE
    
    payback_period = float('inf')
    if yearly_savings > 0:
        payback_period = total_investment / yearly_savings

    return {
        'total_cost': round(total_investment, 2),
        'yearly_savings': round(yearly_savings, 2),
        'payback_period': round(payback_period, 1)
    }