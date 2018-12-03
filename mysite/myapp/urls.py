from django.urls import path
from django.contrib.auth import views as adminviews
from . import views


urlpatterns = [
    path('', views.index),
    path('page/<int:year>/<int:num>/', views.page),
    path('suggestions/', views.rest_suggestion),
    path('comment/<int:suggestion_id>/', views.comment_view),
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
    path('logout/', views.logout_view),
	path('home/', views.home),
	path('Game1/', views.Game1),
	path('Game2/', views.Game2),
	path('Game3/', views.Game3),
	path('Score1/', views.home),
	path('Score2/', views.home),
	path('Score3/', views.home),
	path('Global/', views.home),
]
