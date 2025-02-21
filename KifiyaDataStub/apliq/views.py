import json
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings


# Path to JSON file
JSON_FILE_PATH = os.path.join(settings.BASE_DIR, 'apliq/data/data.json')

# Helper function to load JSON
def load_json():
    with open(JSON_FILE_PATH, 'r') as file:
        return json.load(file)

# Helper function to save JSON
def save_json(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

# API to Fetch JSON Data
@api_view(['GET'])
def get_json_data(request):
    data = load_json()
    return JsonResponse(data, safe=False)

# API to Update a JSON Item
@api_view(['PUT'])
def update_json_item(request, key):
    data = load_json()
    new_value = request.data.get("value")

    if key in data:
        data[key] = new_value
        save_json(data)
        return JsonResponse({"message": f"{key} updated successfully", "data": data})
    
    return JsonResponse({"error": "Key not found"}, status=404)

# API to Delete a JSON Item
@api_view(['DELETE'])
def delete_json_item(request, key):
    data = load_json()

    if key in data:
        del data[key]
        save_json(data)
        return JsonResponse({"message": f"{key} deleted successfully", "data": data})
    
    return JsonResponse({"error": "Key not found"}, status=404)



# import json
# import os
# from django.conf import settings
# from django.http import JsonResponse

# def serve_json(request):
#     """Loads and returns data.json as a JSON response."""
#     json_path = os.path.join(settings.BASE_DIR, 'apliq', 'data', 'data.json')
    
#     try:
#         with open(json_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return JsonResponse(data, safe=False)  # safe=False allows lists at the top level
#     except FileNotFoundError:
#         return JsonResponse({"error": "File not found"}, status=404)
#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON format"}, status=400)








# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import FinancialMetrics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import FinancialMetricsSerializer
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from decimal import Decimal



# # Create your views here.
# def landing(request):
#     return render(request, 'landing.html')

# @api_view(['GET'])
# def api_apliq(request):
#     financial_metrics = FinancialMetrics.objects.all()
#     serializer = FinancialMetricsSerializer(financial_metrics, many=True)
#     return Response(serializer.data)

# decimal_field = openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT)

# @swagger_auto_schema(
#     method='post',
#     request_body=openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         properties={
#             'liquidity_provider_id': decimal_field,
#             'total_funds': decimal_field,
#             'npl': decimal_field,
#             'average_age_borrower': decimal_field,
#             'total_injected_liquidity': decimal_field,
#             'available_liquidity': decimal_field,
#             'liquidity_utilization_rate': decimal_field,
#             'monthly_liquidity_injections': decimal_field,
#             'total_loans_disbursed': decimal_field,
#             'guarantee_utilization_rate': decimal_field,
#             'outstanding_loan_guarantees': decimal_field,
#             'total_pending_liquidity_requests': decimal_field,
#             'total_disbursed_liquidity': decimal_field,
#         },
#         required=['total_funds', 'npl']
#     ),
#     responses={201: openapi.Response("Success", FinancialMetricsSerializer)}
# )


# @api_view(['POST'])
# def create_financial_metrics(request):
#     """
#     API to insert data into FinancialMetrics model.
#     """
#     # print(request.data)
#     serializer = FinancialMetricsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {"message": "Data inserted successfully!", "data": serializer.data},
#             status=status.HTTP_201_CREATED
#         )
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)