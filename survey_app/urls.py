from django.urls import path
from . import views

urlpatterns = [
    path('survey', views.survey),
    path('survey/new', views.new),
]