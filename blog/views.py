from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)

 # Create your views here.

# def home(request):
# 	context={
# 	'posts':Post.objects.all()
# 	}
# 	return render(request,'blog/blog_home.html', context)

class PostListView(ListView):
	model=Post
	template_name='blog/blog_home.html' # <app>/<model>_<viewtype>.html
	context_object_name='posts'
	ordering=['-date_posted']

class PostDetailView(DetailView):
	model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','description']
	template_name='blog/post_data.html'

	def form_valid(self,form):
		# if(self.request.user.is_authenticated):
			form.instance.author=self.request.user
			return super().form_valid(form)
		# else:
		# 	messages.info(self.request,f'First log in your account')
		# 	return redirect('login')

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','description']
	template_name='blog/post_data.html'

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post

	success_url='/blog/'

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False

def about(request):
	return render(request,'blog/blog_about.html')