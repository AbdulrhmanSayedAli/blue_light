from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from .models import Order, Coupon
from .serializers import OrderSerializer, OrderListSerializer, OrderCreateSerializer, CouponSerializer
from .filters import OrderFilter
from rest_framework import status
from rest_framework.response import Response


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "post"]
    permission_classes = [permissions.IsAuthenticated]
    model = Order
    ordering_fields = ["payment_status", "created_at"]
    filterset_class = OrderFilter

    def get_queryset(self):
        queryset = Order.objects.all()
        if self.action == "retrieve":
            queryset = queryset.prefetch_related("courses")
        return queryset

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer

        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer


class CheckCouponView(RetrieveAPIView):
    lookup_field = "code"
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
