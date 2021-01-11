
from rest_framework import routers
from .api import OrderViewSet

router = routers.DefaultRouter()
router.register('api/Orders', OrderViewSet, 'orders')

urlpatterns = router.urls