from django.shortcuts import render
from django.views.generic import TemplateView

class ProblemListView(TemplateView):
    template_name = 'RevisionApp/problem_list.html'