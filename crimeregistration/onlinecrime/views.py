from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import SignUpForm, AddCase, UserForm
from .models import SignUp, Newcase
from django.contrib.auth.forms import UserCreationForm, User
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class HomePageView(TemplateView):

	template_name = "onlinecrime/home.html"

class AboutPageView(TemplateView):
	template_name = "onlinecrime/about.html"

class SignUpFormView(View):
	form_class = SignUpForm
	template_name = "onlinecrime/signup_form.html"

	#display blank form
	def get(self, request):
		signup_form = SignUpForm(None)
		user_form = UserCreationForm(None)
		return render(request, self.template_name, {'user_form': user_form, 'signup_form' : signup_form})

	def post(self, request):
		signup_form = SignUpForm(request.POST)
		user_form = UserCreationForm(request.POST)

		if user_form.is_valid() and signup_form.is_valid():
			user = user_form.save(commit = False)
			signup = signup_form.save(commit=False)
			
			#cleaned (normalised ) data
			
			
			user.save()

			signup.user = user
			signup.save()
			
		return redirect('home')	

def login_user(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				users = SignUp.objects.filter(user=request.user)
				return render(request, 'onlinecrime/user_dashboard.html', {'users': users})
			else:
				return render(request, 'onlinecrime/user_login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'onlinecrime/user_login.html', {'error_message': 'Invalid login'})
	return render(request, 'onlinecrime/user_login.html')
	
def login_employee(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				users = SignUp.objects.filter(user=request.user)
				
				return render(request, 'onlinecrime/employee_dashboard.html', {'users': users})
			else:
				return render(request, 'onlinecrime/employee_login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'onlinecrime/employee_login.html', {'error_message': 'Invalid login'})
	return render(request, 'onlinecrime/employee_login.html')

		#return redirect('home')


class UserDashboardView(TemplateView):
	template_name = "onlinecrime/user_dashboard.html"
	
	


class EmployeeDashboardView(TemplateView):
	template_name = "onlinecrime/employee_dashboard.html"


def logout_user(request):
	logout(request)
	form = UserCreationForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, 'onlinecrime/home.html', context)

class AddCaseView(View):
	form_class = AddCase
	template_name = "onlinecrime/newcase_form.html"

	#display blank form
	def get(self, request):
		addcase_form = AddCase(initial={'username': request.user.username})
		return render(request, self.template_name, { 'addcase_form' : addcase_form})

	def post(self, request):
		addcase_form = AddCase(request.POST, )
		
		
		if addcase_form.is_valid():
			
			addcase = addcase_form.save(commit=False)
			addcase.save()
		return redirect('allcases')	



def AllCases_OfLoggedUserView(request):
	allcases = Newcase.objects.filter(username = request.user.username)
	return render(request, "onlinecrime/allcases.html", { 'allcases' : allcases} )
		
def update_view(request): 
	if request.method == 'GET':
		user = request.user
		account_details = SignUp.objects.filter(user  = user).first()
		username = request.user.username
		password = request.user.password
		user_form = UserCreationForm( initial = {'username': username, 'password1': password, 'password2': password})
		signup_form = SignUpForm(request.GET or None, instance = account_details)
		#signup_form = SignUpForm( request.GET or None, instance = account_details )
		user_form.fields['password1'].widget.render_value = True
		user_form.fields['password2'].widget.render_value = True
		return render(request, 'onlinecrime/update_profile.html', {'signup_form': signup_form, 'user_form': user_form})
	else:
		user_form = UserCreationForm(request.POST)
		signup_form = SignUpForm(request.POST)

		if user_form.is_valid() and signup_form.is_valid():
			user_form.save()
			signup_form.save()

		return redirect('userdashboard')
