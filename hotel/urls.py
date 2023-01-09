from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/',include('api.urls')),
    path('crud_op/',include('crud_operations.urls')),
]
