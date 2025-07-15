import requests
import pandas as pd

def fetch_pvgis_data(lat, lon, peak_power=1.0, loss=14.0):
    """Fetches solar irradiance and PV production data from PVGIS."""
    api_url = "https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"
    params = {
        'lat': lat,
        'lon': lon,
        'peakpower': peak_power,
        'loss': loss,
        'outputformat': 'json',
        'raddatabase': 'PVGIS-SARAH2', # A modern, reliable database
        'angle': 35, # A reasonable default tilt
        'aspect': 0, # South-facing
    }
    
    try:
        response = requests.get(api_url, params=params, timeout=30)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Extract relevant summary data
        summary = data['outputs']['totals']['fixed']
        monthly_data = data['outputs']['monthly']['fixed']

        df_monthly = pd.DataFrame(monthly_data)
        df_monthly.rename(columns={'E_m': 'monthly_production_kwh'}, inplace=True)
        
        return {
            'avg_daily_kwh': summary['E_d'],
            'avg_monthly_kwh': summary['E_m'],
            'total_yearly_kwh': summary['E_y'],
            'monthly_data': df_monthly[['month', 'monthly_production_kwh']]
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching PVGIS data: {e}")
        return None