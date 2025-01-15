from django.urls import path
from . import views

urlpatterns = [
    path('start-task/', views.start_task, name='start_task'),
    path('add/', views.productViews.as_view(), name='stop_task'),
]
