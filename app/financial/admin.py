from django.contrib import admin

from .models import Financial, FinancialType

admin.site.register(Financial)
admin.site.register(FinancialType)
