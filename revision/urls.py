from django.urls import path
from .views import ProblemListView,FilterSearch, SolvedView

urlpatterns = [
    path('', ProblemListView.as_view(), name='revision'),
    path('search/', FilterSearch.as_view(), name='search-filter'),
    path('solved/', SolvedView.as_view(), name='solved'),

]