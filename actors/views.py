from app.permissions import GlobalDefaultPermission
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from .serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()

        try:
            instance.delete()
            return JsonResponse({'message': 'Actor removed sucessfully'}, status=204)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
