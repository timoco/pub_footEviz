from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="football_mapper")

def geolocate(venue_name, city_name):
    """
    Returns a geopy Location object with latitude and longitude
    for a given venue and city name.
    """
    try:
        location = geolocator.geocode(f"{venue_name}, {city_name}, Europe", timeout=10)
        return location
    except GeocoderTimedOut:
        return None
