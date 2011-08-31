# Create your views here.
from models import Frontpage
from django.shortcuts import render_to_response
from django.template import RequestContext

def frontpage(request):
    args = Frontpage.objects.get(id=1)
    return render_to_response('frontpage.html', { 'args': args },context_instance=RequestContext(request))