
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="user",timeout=10)
tosearch="pune"
location = geolocator.geocode(tosearch)
print("The location paramters of {} are latitude={}, longitude={}".format(tosearch,location.latitude, location.longitude))