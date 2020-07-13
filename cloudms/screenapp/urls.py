from django.urls import path
from screenapp import views

urlpatterns = [
    path('',views.screenproc),
]