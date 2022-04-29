
from django.urls import path

from app.views import MainPageView, PortfolioPageView, BlogPageView, BlogDetailView, PortfolioDetailView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='project-detail'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),

]
