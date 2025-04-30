from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add/', views.add_room, name='add_room'),
    path('edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('search/', views.search_room, name='search_room'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
   
]