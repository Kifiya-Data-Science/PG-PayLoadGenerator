from django.db import models
# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField

class FinancialMetrics(models.Model):
    liquidity_provider_id = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_funds = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    npl = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Non-Performing Loans
    number_of_customers = models.IntegerField(null=True)
    total_banks = models.BigIntegerField(default=0)
    average_age_borrower = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    active_guarantees = models.IntegerField(null=True, blank=True)
    total_injected_liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    available_liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    liquidity_utilization_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    monthly_liquidity_injections = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    total_loans_disbursed = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    fund_allocation_per_organization = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    guarantee_utilization_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    outstanding_loan_guarantees = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    loan_performance_metrics = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    total_pending_liquidity_requests = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    total_disbursed_liquidity = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __str__(self):
        return f"Financial Metrics (Total Banks: {self.total_banks})"
