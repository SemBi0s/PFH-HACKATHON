from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View

class HomeView(View):
	def get(self, request, *args, **kwargs):
		try:
			if request.session['logged_in']:
				return redirect('dashboard')
		except KeyError:
			pass

		return render(request, 'index/index.html')

	def post(self,request,*args,**kwargs):
		return HttpResponse("<h1>Page was not found</h1>", status=404)

class DashboardView(View):
	def get(self, request,*args,**kwargs):
		try:
			if request.session['logged_in']:
				return render(request, 'dashboard/index.html')
		except KeyError:
			pass

		return redirect('index')

		def post():
			return HttpResponse("<h1>Page was not found</h1>", status=404)