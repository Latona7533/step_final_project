
from django.urls import path

from app.views import MainPageView, PortfolioPageView, BlogPageView, BlogDetailView, PortfolioDetailView, \
    CommentCreateView, project_detail

urlpatterns = [
    path('', MainPageView.as_view()),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', project_detail, name='project-detail'),
    path('portfolio/add_comment/', CommentCreateView.as_view(), name = 'add_comment'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),

]
