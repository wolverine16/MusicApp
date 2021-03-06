"""myTunes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from tunesApp import views

# urlpatterns = patterns('',)

urlpatterns = [
    #path('accounts/login/', auth_views.my_login),
    # Home page
    path('', views.home),
    path('favorites/', views.favorites),
    path('favorites/songs', views.favSongs),
    path('favorites/songs/<str:song_id>/', views.favSongs),
    path('favorites/artists', views.favArtists),
    path('favorites/artists/<str:artist_id>/', views.favArtists),
    path('favorites/genres', views.favGenres),
    path('favorites/genres/<int:genre_id>/', views.favGenres),
    path('search/', views.search),
    path('search/<str:song_param>/<str:artist_param>/<str:genre_param>/<str:album_param>/',views.search),
    path('search/results', views.results),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('album_info/<int:album_id>/',views.album_info)
    #path('users/', include(('users.urls', 'users'), namespace='users'))
    #path('accounts/', include('userena.urls')),
]   
