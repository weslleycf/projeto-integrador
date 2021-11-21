from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [

    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('search/', SearchResultsView.as_view(), name='search_results')

]
