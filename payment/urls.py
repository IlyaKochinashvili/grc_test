from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from payment.views import PaymentViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'statuses', StatusViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
