from django.urls import path
from . import views
app_name= 'doctor'
urlpatterns = [
    path('', views.docHome, name='docHome'),
       
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)