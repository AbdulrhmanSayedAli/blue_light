from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import AD, Section
from .serializers import ADSerializer, SectionSerializer


class ADViewSet(ReadOnlyModelViewSet):
    model = AD
    queryset = AD.objects.all()
    serializer_class = ADSerializer
    filter_backends = []


class SectionViewSet(ReadOnlyModelViewSet):
    model = Section
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = []
