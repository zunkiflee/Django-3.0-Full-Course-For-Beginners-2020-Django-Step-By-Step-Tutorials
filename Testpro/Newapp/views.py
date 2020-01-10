from django.shortcuts import render, redirect
#from django.shortcuts import HttpResponse
from .models import NewsDB
from .forms import RegistrationForm, RegistrationModal
from .models import RegistrationData
from django.contrib import messages




def NewsP(request):
	obj = NewsDB.objects.get(id=1)

	context = {
		#"list" : ['Python','Java','C++','Html','PHP'],
		#"mynum" : 40
		"data" : obj
	}

	return render(request, 'news.html', context)


def NewsDate(request, year):

	article_list = NewsDB.objects.filter(pub_date__year=year)
	
	context = {
		'year' : year,
		'article_list': article_list
	}

	return render(request, 'newsdate.html', context)


def Home(request):

	context = {
		"name" : "Zunkiflee Waesani",
		"number" : 12345
	}

	return render(request, 'home.html', context)


def Contact(request):
	return render(request, 'contact.html')


def register(request):

	context = {
		"form" : RegistrationForm
	}

	return render(request, 'signup.html', context)


def addUSer(request):
	form = RegistrationForm(request.POST)

	if form.is_valid():
		myregister = RegistrationData(username = form.cleaned_data['username'],
								    password = form.cleaned_data['password'],
			                        email = form.cleaned_data['email'],
			                        phone = form.cleaned_data['phone'])
		myregister.save()

		messages.add_message(request, messages.SUCCESS,	"You Have Singup SuccessFully")

	return redirect('register')


def modelform(request):

	context = {
		"modelform" : RegistrationModal
	}

	return render(request, 'modelform.html', context)


def addModelForm(request):
	mymodelform = RegistrationModal(request.POST)

	if mymodelform.is_valid():
		mymodelform.save()

	return redirect('form')