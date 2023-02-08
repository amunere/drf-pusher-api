from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt import views as jwt_views
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'maillist', views.MaillistViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += doc_urls