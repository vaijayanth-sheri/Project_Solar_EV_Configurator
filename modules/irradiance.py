# solar_configurator/modules/irradiance.py
import requests
import pandas as pd

# Default values that can be overridden by the expert user
DEFAULT_LOSS = 14.0
DEFAULT_TILT = 35.0
DEFAULT_AZIMUTH = 0.0 # 0=South, -90=East, 90=West

def fetch_pvgis_data(
    lat: float, lon: float, 
    peak_power: float = 1.0, 
    loss_override: float = None,
    tilt_override: float = None,
    azimuth_override: float = None
) -> dict or None:
    """
    Fetches PVGIS data, using override values for system parameters if provided.
    """
    api_url = "https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"
    
    # Use override value if provided, otherwise use the module's default
    loss = loss_override if loss_override is not None else DEFAULT_LOSS
    tilt = tilt_override if tilt_override is not None else DEFAULT_TILT
    azimuth = azimuth_override if azimuth_override is not None else DEFAULT_AZIMUTH

    # Automatic Database Switching for global coverage
    database = 'PVGIS-SARAH2' if -60 <= lat <= 65 and -40 <= lon <= 70 else 'PVGIS-ERA5'
    print(f"Using PVGIS database: {database} with Tilt={tilt}, Azimuth={azimuth}, Loss={loss}")

    params = {
        'lat': lat, 'lon': lon, 'peakpower': peak_power, 'loss': loss,
        'outputformat': 'json', 'raddatabase': database,
        'angle': tilt, 'aspect': azimuth,
    }
    
    try:
        response = requests.get(api_url, params=params, timeout=45)
        response.raise_for_status()
        data = response.json()
        
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
        print(f"An error occurred while fetching PVGIS data: {e}")
        return None
