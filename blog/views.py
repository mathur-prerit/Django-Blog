from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
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
	paginate_by=5

class UserPostListView(ListView):
	model=Post
	context_object_name='posts'
	paginate_by=5

	def get_query_set(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		print('----------------------->',user)
		return Post.objects.filter(author=user).order_by('-date_posted')


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