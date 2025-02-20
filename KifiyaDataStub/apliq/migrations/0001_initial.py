# Generated by Django 4.2.19 on 2025-02-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_funds', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('npl', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('number_of_customers', models.IntegerField(blank=True, null=True)),
                ('total_banks', models.BigIntegerField(default=0)),
                ('average_age_borrower', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('active_guarantees', models.IntegerField(blank=True, null=True)),
                ('total_injected_liquidity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('available_liquidity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('liquidity_utilization_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('monthly_liquidity_injections', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_loans_disbursed', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('fund_allocation_per_organization', models.JSONField(blank=True, default=dict)),
                ('guarantee_utilization_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('outstanding_loan_guarantees', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('loan_performance_metrics', models.JSONField(blank=True, default=dict)),
                ('total_pending_liquidity_requests', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_disbursed_liquidity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
    ]
