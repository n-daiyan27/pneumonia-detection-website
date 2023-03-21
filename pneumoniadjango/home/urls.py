from django.urls import path
from . import views
app_name= 'home'
urlpatterns = [
    path('', views.image_view, name='hm'),
    path('', views.delete_image, name='delete')
       
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)