from django_filters import rest_framework as filters
from common.rest_framework.filters import FilterLookupExpr
from .models import Order


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            "payment_status": FilterLookupExpr.OTHER,
        }
