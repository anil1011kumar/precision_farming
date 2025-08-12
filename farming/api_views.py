from rest_framework import generics, filters
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_fertilizer_recommendation
from .irrigation import should_irrigate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer


class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]

class SensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fertilizer_recommendation(request):
    crop_type = request.data.get('crop_type')
    soil_type = request.data.get('soil_type')
    season = request.data.get('season')

    recommendation =  get_fertilizer_recommendation(crop_type, soil_type, season)
    return Response({"recommendation": recommendation})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def is_should_irrigate(request):
    soil_moisture = request.data.get('soil_moisture')
    rain_mm = request.data.get('rain_mm')
    irrigation = should_irrigate(soil_moisture, rain_mm)
    return Response({"should_irrigate": irrigation})

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['soil_type','season']
    search_fields = ['user']

