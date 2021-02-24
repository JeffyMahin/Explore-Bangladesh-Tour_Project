from django.urls import path
from tour_app import views

urlpatterns = [
    path('', views.index, name='division'),
    path('location/', views.location, name='location'),
    path('location/<int:pk>/', views.location_detail, name='location_detail'),
    path('blog/', views.blog, name='blog'),
    path('image/', views.image, name='image'),
    path('tour_guide/', views.tour_guide),
]