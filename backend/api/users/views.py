from rest_framework.viewsets import ReadOnlyModelViewSet
from users.models import City, Univeristy, Specialization
from users.serializers import CitySerializer, UniveristySerializer, SpecializationSerializer


class CityViewSet(ReadOnlyModelViewSet):
    model = City
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UniveristyViewSet(ReadOnlyModelViewSet):
    model = Univeristy
    queryset = Univeristy.objects.all()
    serializer_class = UniveristySerializer


class SpecializationViewSet(ReadOnlyModelViewSet):
    model = Specialization
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
