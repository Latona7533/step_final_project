from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app.models import Profile, Portfolio, Blog


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


class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'detailblog.html'



