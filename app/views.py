from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from app.forms import RequestForm
from app.models import Profile, Portfolio, Blog, Comment


class MainPageView(ListView):
    model = Profile
    template_name = 'index.html'
    context_object_name = 'profile'



class PortfolioPageView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolio'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(descr__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class PortfolioDetailView(DetailView):
    model = Portfolio
    context_object_name = 'project'
    template_name = 'detailproject.html'

class CommentCreateView(CreateView):
    model = Comment
    form_class = RequestForm
    template_name = 'comment.html'
    success_url = '/'


    def form_valid(self, form):
        post = get_object_or_404(Portfolio, pk = self.kwargs ['pk'])
        form.instance.post = Portfolio
        return super().form_valid(form)


class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'detailblog.html'



