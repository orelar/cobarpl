from django.urls import path
from . import views


urlpatterns = [
	path('baca-catatan/', views.index, name="catatan"),
	path('buat-catatan/', views.buatCatatan, name="buat-catatan"),
]