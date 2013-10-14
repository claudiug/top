# Create your views here.

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from .models import Poll


def index(request):
#return HttpResponse("salutare aici este index")
#output = '.'.join([p.question for p in latest_poll])
#return HttpResponse(output)
#template = loader.get_template("index.html")
#context = RequestContext(request, {'latest_poll', latest_poll})
#return HttpResponse(template.render(context))
    latest_poll = Poll.objects.order_by('pub_date')[:5]
    return render(request, "index.html", {'latest_poll' :latest_poll})


def detail(request, poll_id):
    #try:
    #    poll = Poll.objects.get(pk = poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    poll = get_object_or_404(Poll, pk = poll_id)
    return render(request, 'detail.html', {'poll': poll})

def result(request, poll_id):
    return HttpResponse("the result for poll %s" % poll_id)


def vote(request, poll_id):
    return HttpResponse("you are voting for %s" % poll_id)

