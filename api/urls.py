from home.views import index,person,Login
from django.urls import path

urlpatterns = [
    path('index/',index),
    path('person/',person),
    path('login/',Login)
]
