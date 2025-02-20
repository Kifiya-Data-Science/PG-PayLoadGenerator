from django.urls import path,re_path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions




urlpatterns = [
    path('', views.landing, name='landing'),
    path('read/', views.api_apliq),
    path('write/', views.create_financial_metrics, name='insert_financial_metrics'),

    ]