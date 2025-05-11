from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashbord/', include('dashbord.urls')),
    path('signup/', views.signup, name='signup'),
]
