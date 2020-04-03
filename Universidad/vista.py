from django.shortcuts import render

def index(req):
	return render(req, 'index.html', {})

def register(req):
	return render(req, 'register.html', {})

def support(req):
	return render(req, 'support.html', {})