from django.urls import path
from timezonefindertest.views import Index


urlpatterns = [
    path('', Index.as_view(), name='index')
]
