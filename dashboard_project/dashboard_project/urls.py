from django.urls import path
from dashboard import views

urlpatterns = [
   
    path('api/data/', views.get_data, name='get_data'),
    
    path('api/filtered_data/', views.get_filtered_data, name='get_filtered_data'),
]