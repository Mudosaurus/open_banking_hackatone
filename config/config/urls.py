from django.contrib import admin
from django.urls import path, include

from hob_api.services import get_swagger_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('e_bank/', include('e_bank.urls')),
    path('style_bank/', include('style_bank.urls')),
    path('consents/', include('consent_service.urls')),
    path('hob_api/', include('hob_api.urls')),
    path('docs/', get_swagger_schema_view().with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]
