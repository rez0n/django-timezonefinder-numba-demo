import time
import os
import django
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from timezonefindertest.models import Airport


# Filter objects that have both lat and lon

airports_w_lat_lon = Airport.objects.filter(
    ~Q(latitude=0.0) & ~Q(longitude=0.0)
)

# Cut first 400 objects
airports_first_400 = airports_w_lat_lon[:400]

# Put objects into template variable
airports = airports_first_400

start_time = time.time()
for airport in airports:
    print(airport.timezone)

print("--- Execution time: %s seconds ---" % (time.time() - start_time))
