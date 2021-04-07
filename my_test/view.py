from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

import datetime 

#import sys
# print sys.path

def current_datetime(request):
    now=datetime.datetime.now()
    t=get_template('current_datetime.html')
    html=t.render({'current_date':now})
    
    ##better WAY
    return render_to_response('current_datetime.html',{'current_datetime':now})

    #return HttpResponse(html)


def hours_ahead(request,offset):
    offset=int(offset)
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>It's now %s then offset %s.</body></html>" % (offset,dt)
    
    return HttpResponse(html)
