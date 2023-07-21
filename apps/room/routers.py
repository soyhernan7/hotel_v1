# room/routers.py
from rest_framework.routers import DefaultRouter
from apps.room.views import RoomViewSet

router = DefaultRouter()
router.register('', RoomViewSet, basename='rooms')

urlpatterns = router.urls