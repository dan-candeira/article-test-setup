from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.http.response import JsonResponse
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import MethodNotAllowed, ParseError

from endpoint.patient.models import Patient
from endpoint.equipment.models import Equipment
from endpoint.loan_history.models import LoanHistory
from endpoint.collect.models import Collect
from endpoint.sensor.models import Sensor
from endpoint.sample.models import Sample


@api_view(['DELETE'])
@renderer_classes((JSONRenderer, BrowsableAPIRenderer, ))
def destroy(request, *args, **kwargs):
    try:
        LoanHistory.objects.all().delete()
        Sample.objects.all().delete()
        Collect.objects.all().delete()
        Sensor.objects.all().delete()
        Equipment.objects.all().delete()
        Patient.objects.all().delete()
    except:
        print('errrrrrrrrrrrrrrrorrrrr!')
        raise ParseError('Something happened')
    return JsonResponse({'message': 'deleted with success.'},
                        status=HTTP_204_NO_CONTENT)
