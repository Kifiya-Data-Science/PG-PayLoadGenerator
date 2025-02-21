from django.shortcuts import render
from rest_framework import viewsets
from .models import FinancialMetrics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FinancialMetricsSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from decimal import Decimal



# Create your views here.
def landing(request):
    return render(request, 'landing.html')

@api_view(['GET'])
def api_apliq(request):
    financial_metrics = FinancialMetrics.objects.all()
    serializer = FinancialMetricsSerializer(financial_metrics, many=True)
    return Response(serializer.data)

decimal_field = openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'liquidity_provider_id': decimal_field,
            'total_funds': decimal_field,
            'npl': decimal_field,
            'average_age_borrower': decimal_field,
            'total_injected_liquidity': decimal_field,
            'available_liquidity': decimal_field,
            'liquidity_utilization_rate': decimal_field,
            'monthly_liquidity_injections': decimal_field,
            'total_loans_disbursed': decimal_field,
            'guarantee_utilization_rate': decimal_field,
            'outstanding_loan_guarantees': decimal_field,
            'total_pending_liquidity_requests': decimal_field,
            'total_disbursed_liquidity': decimal_field,
        },
        required=['total_funds', 'npl']
    ),
    responses={201: openapi.Response("Success", FinancialMetricsSerializer)}
)


@api_view(['POST'])
def create_financial_metrics(request):
    """
    API to insert data into FinancialMetrics model.
    """
    # print(request.data)
    serializer = FinancialMetricsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Data inserted successfully!", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)