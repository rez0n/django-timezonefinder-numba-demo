from django.db import models
from timezonefinder import TimezoneFinder
import pytz


class Airport(models.Model):
    # Incomplete model for testing purposes
    latitude = models.DecimalField(max_digits=6, decimal_places=3, db_column='lat_decimal')
    longitude = models.DecimalField(max_digits=6, decimal_places=3, db_column='lon_decimal')

    class Meta:
        managed = False
        db_table = 'airports'

    @property
    def timezone(self):
        tf = TimezoneFinder()
        tz = tf.timezone_at(lng=float(self.longitude),
                            lat=float(self.latitude))
        timezone = pytz.timezone(tz)
        return timezone
