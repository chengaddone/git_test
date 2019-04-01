from django.http import HttpResponse


def index(request):
	return HttpResponse('index')
	

def add(request):
	return HttpResponse('add')