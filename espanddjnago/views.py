from django.shortcuts import render
import requests
from .models import TempLog
from django.http import JsonResponse
def index(request):
    db_dat = TempLog.objects.order_by('-time')[:10]
    context = {
        'times': [obj.time.strftime('%H:%M') for obj in db_dat][::-1],
        'temp': [obj.val for obj in db_dat][::-1]
    }
    return render(request, 'espanddjnago/index.html', context)
def control(request, state):
    try:
        if state == "wenton":
            response = requests.get("http://192.168.1.73/wenton", timeout=5)
            return JsonResponse({
                'status': 'success',
                'response': response.text,
            })
        elif state == "wentoff":
            response = requests.get("http://192.168.1.73/wentoff", timeout=5)
            return JsonResponse({
                'status': 'success',
                'response': response.text,
            })
        elif state == "sensors":
            return sensors(request)
        else:
            return JsonResponse({
                "status": "error",
                'state': state
            })
    except Exception as e:
        return JsonResponse({
            'starus': 'error',
            'message': str(e),
        })
def sensors(request):
    response = requests.get("http://192.168.1.73/sensors", timeout=9)
    TempLog.objects.create(val=response.text)
    return JsonResponse({
            'status': 'success',
            'value': response.text,
            })

# Create your views here.
