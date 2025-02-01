from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import AD, Section
from .serializers import ADSerializer, SectionSerializer, HomeSerializer
from rest_framework.response import Response
from rest_framework import generics


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


class HomeAPIView(generics.GenericAPIView):
    serializer_class = HomeSerializer

    def get(self, request, *args, **kwargs):
        sections = Section.objects.all()
        ads = AD.objects.all()
        # Note: pass the data via the "instance" parameter for serialization
        serializer = self.get_serializer(instance={"sections": sections, "ads": ads})
        return Response(serializer.data)
