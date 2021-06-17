from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.models import User
from api.models import Team
from django.views.generic.base import TemplateView
from django.views import View

class TeamAddView(View):
	def get(self, request, *args,**kwargs):
		return redirect('index')

	def post(self, request, *args,**kwargs):
		r = request.POST
		try:
			if request.session['logged_in']:
				try:
					teams = Team.objects.all()
					try:
						for i in teams:
							if User.objects.get(id=request.session['userid']) in i.members.all():
								return HttpResponse('You are already in a team')
					except:
						print("No Team")

				except User.DoesNotExist:
					pass
				
				try:
					team = Team.objects.create(name=r.get('teamname'), owner=User.objects.get(id=request.session['userid']))
					team.members.add(User.objects.get(id=request.session['userid']))
					return redirect('dashboard')

				except:
					pass

		except KeyError:
			return redirect('index')

		return redirect('dashboard')

class TeamRemoveView(View):
	def get(self, request, *args,**kwargs):
		return redirect('index')
	def post(self, request, *args,**kwargs):
		pass