from django.urls import path

from . import views


urlpatterns = [
	path('', views.SignUp),
	path('signup/', views.SignUp, name='signup'),
]
