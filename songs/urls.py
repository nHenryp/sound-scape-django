from django.urls import path
from .views import SongListCreateView, SongRetrieveUpdateDestroyView

urlpatterns = [
    path('', SongListCreateView.as_view()),
    path('<int:pk>/', SongRetrieveUpdateDestroyView.as_view())
]