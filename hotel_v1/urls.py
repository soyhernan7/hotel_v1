# hotel_v1/urls.py
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="APIS de DE RESERVAS PARA HOTEL",
        default_version='v1',
        description="Documentación de la API de USER, ROOM, BOOKING Y INVOICE",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/rooms/', include('apps.room.routers')),
    path('api/users/', include('apps.user.routers')),
    path('api/booking/', include('apps.booking.routers')),
    path('api/invoices/', include('apps.invoice.routers')),
    # URLs de Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
