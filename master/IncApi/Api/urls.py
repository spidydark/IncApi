from django.urls import path,include
from Api import views 
from rest_framework.routers import DefaultRouter
from Api import views
router=DefaultRouter()

router.register('viewset',views.ApiView1)
urlpatterns = [
    path('',include(router.urls)),
]
