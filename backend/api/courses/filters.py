from django_filters import rest_framework as filters
from common.rest_framework.filters import FilterLookupExpr
from .models import Course
from django.db.models import Sum


class CourseFilter(filters.FilterSet):
    price__lte = filters.NumberFilter(method="filter_price_lte")
    price__gte = filters.NumberFilter(method="filter_price_gte")

    def inject_price_in_query_set(self, queryset):
        return queryset.annotate(total_price=Sum("videos__price") + Sum("files__price"))

    def filter_price_lte(self, queryset, name, value):
        queryset = self.inject_price_in_query_set(queryset)
        return queryset.filter(total_price__lte=value)

    def filter_price_gte(self, queryset, name, value):
        queryset = self.inject_price_in_query_set(queryset)
        return queryset.filter(total_price__gte=value)

    class Meta:
        model = Course
        fields = {
            "teacher": FilterLookupExpr.OTHER,
        }
