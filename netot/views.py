import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


#Logger
logger = logging.getLogger(__name__)


#Save Incoming data from IOT
@csrf_exempt
def device_data(request):
    
    if request.method == 'POST':
        print("Here's the data: ", request.body) # Logo to a file
        print("################")
        logger.info('This is something')
        return HttpResponse('Done')
    
    else:
        return  HttpResponse('Error')