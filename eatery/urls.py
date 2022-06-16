from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_page, name='home'),
    path('reservations', views.reservation_list.as_view(), name='reservations'),
    path('make_reservation', views.make_reservation, name='make_reservation'),
    path('edit_reservation/<i_id>', views.edit_reservation, name='edit_reservation'),
    path('delete_reservation/<i_id>', views.delete_reservation, name='delete_reservation')
]
