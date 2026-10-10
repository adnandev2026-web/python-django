from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]

# Add this line at the end to serve uploaded files in development mode
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
