from home.views import index,person,Login,PeopleViewSet,RegisterAPI,LoginAPI,PersonAPI
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'people',PeopleViewSet,basename='people')
urlpatterns=router.urls

urlpatterns = [
    path('index/',index),
    path('person/',person),
    # path('login/',Login),
    path('',include(router.urls)),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('persons/',PersonAPI.as_view()),
]
