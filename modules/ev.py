# modules/ev.py

# Constants based on the new prompt
ENERGY_CONSUMPTION_PER_KM = 0.17  # kWh/km
YEARLY_YIELD_PER_KWP = 1000       # kWh/year, a conservative estimate for upsizing yield

def calculate_ev_requirements(num_ev: int, daily_km: int, base_system_yield_kwh: float):
    """
    Calculates EV energy needs and the required *additional* PV system size,
    only if the base system yield is insufficient.
    """
    if num_ev <= 0 or daily_km <= 0:
        return {
            "daily_need_kwh": 0,
            "annual_need_kwh": 0,
            "extra_kwp_needed": 0,
            "additional_yield_kwh": 0,
            "is_sufficient": True,
        }

    # Calculate total annual energy need for all EVs
    daily_need = num_ev * daily_km * ENERGY_CONSUMPTION_PER_KM
    annual_need = daily_need * 365

    # Check if the base system is already sufficient
    energy_deficit = annual_need - base_system_yield_kwh
    
    extra_kwp = 0
    additional_yield = 0
    is_sufficient = True

    if energy_deficit > 0:
        # If there's a deficit, calculate the extra kWp needed to cover it
        is_sufficient = False
        extra_kwp = energy_deficit / YEARLY_YIELD_PER_KWP
        additional_yield = extra_kwp * YEARLY_YIELD_PER_KWP
    
    return {
        "daily_need_kwh": round(daily_need, 2),
        "annual_need_kwh": round(annual_need, 0),
        "extra_kwp_needed": round(extra_kwp, 2),
        "additional_yield_kwh": round(additional_yield, 0),
        "is_sufficient": is_sufficient,
    }