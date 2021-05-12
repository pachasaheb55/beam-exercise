from django.urls import path
from . import views
# URLs for the APIs
urlpatterns = [
    path('exercise1/', views.exercise1_beam),
    path('exercise2/', views.exercise2_beam),
    path('saveScooters/', views.save_scooters),
    path('retrieveScooters/', views.retrieve_scooters),
    path('searchScooters/<lat>/<long>/<int:distance>/<str:measurement>/', views.search_scooters),
]
