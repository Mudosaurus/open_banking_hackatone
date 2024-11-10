from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test_models', views.TestModelViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'valutes', views.ValuteViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'loans', views.LoanViewSet)
router.register(r'salaries', views.SalaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
