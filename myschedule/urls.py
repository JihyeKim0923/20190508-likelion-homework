from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('schedule/<int:schedule_id>/', views.detail, name='detail'),
    path('schedule/new/', views.new, name='new'),
    path('schedule/<int:schedule_id>/edit/', views.edit, name='edit'),
    path('schedule/<int:schedule_id>/delete/',views.delete, name='delete'),
]
