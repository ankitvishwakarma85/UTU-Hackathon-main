from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView , CompanyDetailView ,EnrolledListView, CompanyQueryListView ,NewsDeleteView, QueryCreateView , QueryDeleteView , QueryDeleteView , QueryUpdateView , CompanyCreateView, CompanyUpdateView,NewsUpdateView, CompanyDeleteView, NewsCreateView

urlpatterns = [
    path('',views.dashboard , name = 'TPO-dashboard'),
    path('home/', NewsListView.as_view() , name = 'TPO-home'),
    path('about/', views.about, name = 'TPO-about'),
    path('analytics/', views.analytics, name = 'TPO-analytics'),
    path('news/<int:pk>/', NewsDetailView.as_view() , name = 'news-detail'),
    path('company/<int:pk>/', CompanyDetailView.as_view() , name = 'company-detail'),
    path('company/<str:title>', CompanyQueryListView.as_view() , name = 'company-queries'),
    path('enrolled/<str:title>/', views.enrolled , name = 'enrolled-create'),
    path('query/<str:title>/new/', QueryCreateView.as_view() , name = 'query-create'),
    path('company/new/', CompanyCreateView.as_view() , name = 'company-create'),
    path('company/<int:pk>/update', CompanyUpdateView.as_view() , name = 'company-update'),
    path('company/<int:pk>/delete', CompanyDeleteView.as_view() , name = 'company-delete'),
    path('query/<int:pk>/update/', QueryUpdateView.as_view() , name = 'query-update'),
    path('query/<int:pk>/delete/', QueryDeleteView.as_view() , name = 'query-delete'),
    path('search/news', views.searchnews, name = 'searchnews'),
    path('news/new/', NewsCreateView.as_view() , name = 'news-create'),
    path('news/<int:pk>/update', NewsUpdateView.as_view() , name = 'news-update'),
    path('news/<int:pk>/delete', NewsDeleteView.as_view() , name = 'news-delete'),
    path('enrolled/applicants/<str:title>/', EnrolledListView.as_view() , name = 'enrolled-user'),
]
