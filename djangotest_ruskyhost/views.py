from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello Ruskyhost</h1><p>Django test application</p>")
