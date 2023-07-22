# user/routers.py
from rest_framework.routers import DefaultRouter
from apps.user.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, basename="users")
urlpatterns = router.urls