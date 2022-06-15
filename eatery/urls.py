from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_page, name='home'),
    path('make-reservation', views.reservation_list.as_view(), name='reservation')
]
