from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_page, name='home'),
    path('make-reservation', views.ReservationList.as_view(), name='reservation')
]
