import json
from django.http import JsonResponse
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    def delete(self, *args, **kwargs):
        instance = self.get_object()
        
        try:
            instance.delete()
            return JsonResponse({"message":"Genre removed sucessfully"}, status=204)
        except Exception as e:
            return JsonResponse({"error": str(e)}, staus=500)