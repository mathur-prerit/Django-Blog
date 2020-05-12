from django.shortcuts import render
from django.http import HttpResponse


posts=[
	{
	'author':'Prerit Mathur',
	'title':'Sample Post 1',
	'description':'It is the first sample post',
	},
	{
	'author':'Charu Mathur',
	'title':'Sample Post 2',
	'description':'It is the second sample post',
	}
]

# Create your views here.

def home(request):
	context={
	'posts':posts
	}
	return render(request,'blog/blog_home.html', context)

def about(request):
	return HttpResponse('<h2>about page</h2>')