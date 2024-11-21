from django.contrib import admin
from django.urls import path, include

from hob_api.services import get_swagger_schema_view


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/e_bank/', include('e_bank.urls')),
    path('api/style_bank/', include('style_bank.urls')),
    path('api/consents/', include('consent_service.urls')),
    path('api/hob_api/', include('hob_api.urls')),
    path('api/docs/', get_swagger_schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
