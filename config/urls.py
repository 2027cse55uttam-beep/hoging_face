from django.contrib import admin
from django.urls import path, include  # <-- Yahan 'include' add karna na bhoolein

from django.conf.urls import handler404, handler500 # <-- Import zaroori hai
from core.views import custom_404, custom_500        # <-- Views import karein

urlpatterns = [
    path('secure-dashboard-login/', admin.site.urls),
    
    # Ye line project ko 'core' app ke URLs se jodti hai
    path('', include('core.urls')), 
]

# Ye 2 lines batayengi ki Error aane par kaunsa view chalana hai
handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'