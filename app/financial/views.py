from django.db.models import Q
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Financial


class FinancialDataTable(TemplateView):
    template_name = "financial/datatable.html"


class FinancialDataTableJson(BaseDatatableView):
    model = Financial

    columns = ['created_at', 'type', 'name', 'value']
    order_columns = ['created_at', 'name']

    def get_initial_queryset(self):
        return Financial.objects.all()

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
        return qs
