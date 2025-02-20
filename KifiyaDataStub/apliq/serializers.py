from rest_framework import serializers
from .models import FinancialMetrics

class FinancialMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialMetrics
        fields = '__all__'
    # Convert Decimal fields to float
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field in self.fields:
            if isinstance(self.fields[field], serializers.DecimalField):
                data[field] = float(data[field]) if data[field] is not None else None
        return data