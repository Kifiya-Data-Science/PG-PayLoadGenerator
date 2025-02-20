from django.db import models
# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField

class FinancialMetrics(models.Model):
    liquidity_provider_id = models.CharField(max_length=20, null=True, blank=True)
    total_funds = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    npl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Non-Performing Loans
    number_of_customers = models.IntegerField(null=True, blank=True)
    total_banks = models.BigIntegerField(default=0)
    average_age_borrower = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active_guarantees = models.IntegerField(null=True, blank=True)
    total_injected_liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    available_liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    liquidity_utilization_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    monthly_liquidity_injections = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    total_loans_disbursed = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    fund_allocation_per_organization = JSONField(default=dict, blank=True)
    guarantee_utilization_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    outstanding_loan_guarantees = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    loan_performance_metrics = JSONField(default=dict, blank=True)
    total_pending_liquidity_requests = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    total_disbursed_liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Financial Metrics (Total Banks: {self.total_banks})"
