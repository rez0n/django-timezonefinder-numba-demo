from django.db.models import Q
from django.views.generic.base import TemplateView
from .models import Airport


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter objects that have both lat and lon
        airports_w_lat_lon = Airport.objects.filter(
            ~Q(latitude=0.0) & ~Q(longitude=0.0)
        )

        # Cut first 400 objects
        airports_first_400 = airports_w_lat_lon[:400]

        # Put objects into template variable
        context['airports'] = airports_first_400
        return context
