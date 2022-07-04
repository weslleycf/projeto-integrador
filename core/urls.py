from django.urls import path
from . import views
from .views import SearchResultsView, ProfileDetailView
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', cache_page(60*5)(views.home), name='home'),
    path('accounts/profile/', cache_page(60*5)(views.profile), name='profile'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile_detail')

]
