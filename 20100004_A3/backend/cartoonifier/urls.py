from django.urls import path
from . import views

urlpatterns = [
    path('cartoon/', views.cartoon),
    path('bw/',views.bw),
    #Add a new route below this
    
]