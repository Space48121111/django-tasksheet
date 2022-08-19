from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

def index(request):
    # return HttpResponse("Hello world!")
    # template = loader.get_template('first.html')
    # return HttpResponse(template.render())
    mem = Members.objects.all().values()
    # output = ""
    # for x in mem:
    #     output += x["firstname"]
    # return HttpResponse(output)
    template = loader.get_template('index.html')
    context = {
    'mem': mem,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  mem = Members(firstname=x, lastname=y)
  mem.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  mem = Members.objects.get(id=id)
  mem.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mem = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mem': mem,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  mem = Members.objects.get(id=id)
  mem.firstname = first
  mem.lastname = last
  mem.save()
  return HttpResponseRedirect(reverse('index'))

# end
