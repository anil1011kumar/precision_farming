from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import farmer_input, fertiliser_view
from . import api_views

 


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('farmer/', farmer_input, name='farmer_input'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.register_view, name='register'),
    path('fertiliser_recommendation/',views.fertiliser_view, name='fertliser'),
    path('sensor-data/',api_views.SensorDataListCreateView.as_view(), name = 'sensor-data-list'),
    path('sensor-data/<int:pk>/',api_views.SensorDataDetailView.as_view(), name = 'sensor-data-detail'),
    path('fertiliser-recommendation/',api_views.fertilizer_recommendation, name = 'fertiliser-recommendation'),
    path('should_irrigate/',api_views.is_should_irrigate, name='should_irrigate'),
]