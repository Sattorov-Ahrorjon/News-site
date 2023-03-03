from django.urls import path
from .views import *

urlpatterns = [
    path('', get_index, name='home_page'),
    path('blog/', get_blog, name='blog_page'),
    path('single/<slug:slug>/', get_single, name='single_page'),
    path('blog/category/<slug:slug>/', get_category, name='category_page'),
]


urlpatterns += (
    path('search-result/', SearchResultsListView.as_view(), name='search_result_page'),
)