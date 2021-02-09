
from django.contrib import admin
from django.urls import path, include
from apps import views
from apps.views import index, logins, home, log
from apps.views import UserRegisterView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', include('django.contrib.auth.urls')),
   
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="logins"),
    path('profile/', views.log, name="log"),
    
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
