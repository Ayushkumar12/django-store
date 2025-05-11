from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('dashbord/', admin.site.urls),
    path('', views.dashbord ,name="dashbord"),
    path('home/', views.home ,name="home"),
    path('order/', views.order ,name="home")


]