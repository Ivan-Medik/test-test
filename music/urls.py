from django.contrib import admin
from django.urls import path, include

from .views import home


urlpatterns = [

	path('', home),
#	path('/login/vk-oauth2/', include('social_django.urls')),

]
