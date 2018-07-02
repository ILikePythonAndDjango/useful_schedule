from django.shortcuts import render

from .ajax import HttpResponseAjax, HttpResponseAjaxError

def goals(request):

	return HttpResponseAjax(key='value')