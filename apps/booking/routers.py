# routers.py
from rest_framework.routers import DefaultRouter
from apps.booking.views import BookingViewSet
router = DefaultRouter()
router.register('', BookingViewSet, basename="booking")

urlpatterns = router.urls