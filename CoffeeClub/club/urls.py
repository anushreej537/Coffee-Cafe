from django.urls import path
from club import views

urlpatterns = [
    path('',views.index),
    path('createuser/',views.createuser),
    path('showuser/',views.showuser)
]

