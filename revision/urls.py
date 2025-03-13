from django.urls import path
from .views import ProblemListView,FilterSearch

urlpatterns = [
    path('', ProblemListView.as_view(), name='revision'),
    path('search/', FilterSearch.as_view(), name='search-filter'),

]