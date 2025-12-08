from django.contrib import admin
from django.urls import path, include  # <-- Yahan 'include' add karna na bhoolein

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ye line project ko 'core' app ke URLs se jodti hai
    path('', include('core.urls')), 
]