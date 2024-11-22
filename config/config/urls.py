from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def get_swagger_schema_view() -> type:
    return get_schema_view(
        openapi.Info(
            title="BlackCubics / Сервис согласий",
            description="Open Baning Api (team87)",
            default_version='v1',
        ),
        public=True,
        permission_classes=[permissions.AllowAny,],
    )


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/e_bank/', include('e_bank.urls')),
    path('api/style_bank/', include('style_bank.urls')),
    path('api/consents/', include('consent_service.urls')),
    path('api/docs/', get_swagger_schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
