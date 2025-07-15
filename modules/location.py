from geopy.geocoders import Nominatim
import time

def geocode_address(address):
    """Geocodes an address string to latitude and longitude."""
    geolocator = Nominatim(user_agent="solar_configurator_app")
    try:
        # Adding a delay to respect API usage policies
        time.sleep(1) 
        location = geolocator.geocode(address)
        if location:
            return {
                "address": location.address,
                "latitude": location.latitude,
                "longitude": location.longitude
            }
        else:
            return None
    except Exception as e:
        print(f"Error during geocoding: {e}")
        return None