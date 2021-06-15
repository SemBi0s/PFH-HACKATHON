from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View

class UserRegisterView(View):
	def get(self, request, *args, **kwargs):
		try:
			if request.session['logged_in']:
				return render(request, 'dashboard/index.html')
		except KeyError:
			pass		
		
		return render(request, 'register/index.html')
		

	def post(self, request, *args, **kwargs):
		if request.session['logged_in']:
			return render(request, 'dashboard/index.html')
			
		r = request.POST
		username = r.get('username')
		password = r.get('password')
		email = r .get('email')
		first_name = r .get('first_name')
		last_name = r.get('last_name')

		if username == "":
			return HttpResponse("missing username")
		if password == "":
			return HttpResponse("missing password")
		if email == "":
			return HttpResponse("missing email")
		if first_name == "":
			return HttpResponse("missing first_name")
		if last_name == "":
			return HttpResponse("missing last_name")

		User = get_user_model()
		users = User.objects.all()
		for i in users:
			if i.get_username() == username:
				return HttpResponse("Username already taken")
	
		
		user = User.objects.create_user( username, email=email, password=password, first_name=first_name, last_name=last_name)
		user.save()
		return redirect('Login')

class UserLoginView(View):
	def get(self, request, *args, **kwargs):
		try:
			if request.session['logged_in']:
				return redirect('dashboard')
		except KeyError:
			pass

		return render(request, 'login/index.html')

	def post(self, request ,*args, **kwargs):
		try:
			if request.session['logged_in']:
				return redirect('dashboard')
		except KeyError:
			pass

		r = request.POST
		username = r.get('username')
		password =  r.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			request.session['userid'] = user.id
			request.session['logged_in'] = True
			return redirect('index')
		else:
			return HttpResponse("Wrong Username or Password")

class UserLogoutView(View):
	def post(self, request, *args, **kwargs):
		return HttpResponse("<h1>Page was not found</h1>", status=404)

	def get(self, request, *args, **kwargs):
		try:
			if request.session['logged_in']:
				del request.session['logged_in']
				del request.session['userid']
				return redirect('index')

		except KeyError:
			pass

		return redirect('index')