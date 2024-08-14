from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),  # Include URLs from the news app
    path('users/', include('users.urls')),  # Include URLs from the users app
]