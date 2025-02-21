from django.urls import path,re_path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions




urlpatterns = [
    # path('', views.landing, name='landing'),
    # path('read/', views.api_apliq),
    # path('write/', views.create_financial_metrics, name='insert_financial_metrics'),
    # path('servedummy/', views.serve_json, name='serve_json')
    ]

urlpatterns = [
    path('servedummy/', views.get_json_data, name='get-json-data'),
    path('update/<str:key>/', views.update_json_item, name='update-json-item'),
    path('delete/<str:key>/', views.delete_json_item, name='delete-json-item'),
]