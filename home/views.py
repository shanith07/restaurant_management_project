from django.shortcuts import render
from rest-framework .respone import Response
from rest-framework .views import APIView
from .serializers import RestaurantInfoSerializer


# Create your views here.
class HomepageView(APIView):
    def get(self, request):
        info=RestaurantInfo.objects.first()
        if info:
            serializer=RestaurantInfoSerializer(info)
            return Response(serializer.data)
        return Response({"name": "Restaurant name not set"})