from rest_framework.routers import DefaultRouter
from django.urls import path, include

from endpoint.patient.views import PatientViewSet
from endpoint.equipment.views import EquipmentViewSet
from endpoint.collect.views import CollectViewSet
from endpoint.loan_history.views import LoanHistoryViewSet
from endpoint.sample.views import SampleViewSet
from endpoint.sensor.views import SensorViewSet
from endpoint.delete_all.views import destroy


app_name = 'api'
router = DefaultRouter()

router.register('patients', PatientViewSet)
router.register('equipments', EquipmentViewSet)
router.register('collects', CollectViewSet)
router.register('loans-history', LoanHistoryViewSet)
router.register('samples', SampleViewSet)
router.register('sensors', SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('delete/', destroy, name='delete-all')
]
