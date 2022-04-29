
from django.urls import path

from app.views import MainPageView, PortfolioPageView, BlogPageView, BlogDetailView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
]
