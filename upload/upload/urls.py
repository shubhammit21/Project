from api.views import PersonViewSet
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from api import views

router = routers.DefaultRouter()
router.register('person', PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', include(router.urls)),
    path('', include(router.urls)),
   # path('', views.simple_upload),
]