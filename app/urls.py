from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDeleteView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy'),
    
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDeleteView.as_view(), name='actor-retrieve-update-destroy'),
    
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy'),
]
