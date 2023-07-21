# routers.py
from rest_framework.routers import DefaultRouter
from apps.invoice.views import InvoiceViewSet

router = DefaultRouter()
router.register('', InvoiceViewSet, basename='invoices')

urlpatterns = router.urls
