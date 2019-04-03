from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('start_game', views.start_game, name = 'start_game'),
    path('game/<int:pk>/', views.GameView.as_view(), name = 'game'),
    path('make_move/<int:pk>/', views.make_move, name = 'make_move')
]