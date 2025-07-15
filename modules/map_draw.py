import folium
from folium.plugins import Draw
from shapely.geometry import Polygon
import pyproj

def display_map(center_lat, center_lon, zoom=20):
    """
    Creates and displays a Folium map with drawing tools.
    The Draw() plugin is called with NO arguments, which is the most robust
    method to prevent JSON serialization errors across library versions.
    """
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=zoom,
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Esri",
        scrollWheelZoom=True,
    )

    Draw().add_to(m)
    
    return m

def calculate_polygon_area(geojson_data):
    """
    Calculates the area of a GeoJSON polygon in square meters.
    """
    if not geojson_data or 'geometry' not in geojson_data:
        return 0
    try:
        polygon = Polygon(geojson_data['geometry']['coordinates'][0])
    except Exception:
        return 0
    if polygon.is_empty or not polygon.is_valid:
        return 0
    source_crs = pyproj.CRS("EPSG:4326")
    utm_zone = int((polygon.centroid.x + 180) / 6) + 1
    if polygon.centroid.y < 0:
        utm_crs = pyproj.CRS(f"EPSG:327{utm_zone}")
    else:
        utm_crs = pyproj.CRS(f"EPSG:326{utm_zone}")
    transformer = pyproj.Transformer.from_crs(source_crs, utm_crs, always_xy=True)
    projected_polygon = Polygon(transformer.itransform(polygon.exterior.coords))
    return projected_polygon.area