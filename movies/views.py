from django.http import JsonResponse
from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def delete(sef, *args, **kwargs):
        instance = self.get_object()
        
        try:
            instance.delete()
            return JsonResponse({'message': 'Movie removed sucessfully'}, status=204)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    

