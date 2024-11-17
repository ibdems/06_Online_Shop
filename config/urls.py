
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shop.urls')),
    path('accounts/', include('users.urls')),
    path('', include('admin_volt.urls')),
    path('admin/', admin.site.urls),
   
]
