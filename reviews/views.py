from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def delete(self, *args, **kwargs):
        instance = self.get_object()
        
        try:
            instance.delete()
            return JsonResponse({'message': 'Review removed sucessfully'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)