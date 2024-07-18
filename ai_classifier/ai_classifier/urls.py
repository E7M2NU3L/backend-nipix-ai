from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ai_sentiment/', include('nipix_ai.urls'))
]
