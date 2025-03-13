from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from .problemGen import GenerateProblems
from .models import Solved
import os
import time
from django.contrib import messages


class ProblemListView(View):
    template_name = 'RevisionApp/problem_list.html'

    def get(self,request):
        problem_query = "list top 10 DSA problems"
        problem_lst={}
        try:

            problem_lst = GenerateProblems(problem_query)
            print(problem_lst)
        except Exception as e:
            print(e)
            # time.sleep(0)

            problem_lst= [{'title': 'Two Sum', 'description': 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.', 'link': 'https://leetcode.com/problems/two-sum/', 'frequency': 5}, {'title': 'Reverse Linked List', 'description': 'Given the head of a singly linked list, reverse the list, and return the reversed list.', 'link': 'https://leetcode.com/problems/reverse-linked-list/', 'frequency': 4}, {'title': 'Valid Parentheses', 'description': "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.", 'link': 'https://leetcode.com/problems/valid-parentheses/', 'frequency': 3}, {'title': 'Merge Intervals', 'description': 'Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.', 'link': 'https://leetcode.com/problems/merge-intervals/', 'frequency': 2}, {'title': 'Binary Tree Inorder Traversal', 'description': "Given the root of a binary tree, return the inorder traversal of its nodes' values.", 'link': 'https://leetcode.com/problems/binary-tree-inorder-traversal/', 'frequency': 1}]
            # os.system('ollama run deepseek-r1')

        context={
            "problems": problem_lst,
        }
        if request.htmx:
            return render(request,'RevisionApp/problem_list.html#problemsComponent',context=context)
        return render(request,self.template_name)
    

class FilterSearch(View):
    def get(self,request):
        search = request.GET.get('search')
        difficulty = ""
        if request.GET.get('difficulty'):
            difficulty = request.GET.get('difficulty')
            print(difficulty)
        problem_query = f"list top 10 {difficulty} {search} problems"
        problem_lst={}
        try:

            problem_lst = GenerateProblems(problem_query)
            print(problem_lst)
        except Exception as e:
            # time.sleep(6)
            print(e)
            # problem_lst= [{'title': 'Two Sum', 'description': 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.', 'link': 'https://leetcode.com/problems/two-sum/', 'frequency': 5}, {'title': 'Reverse Linked List', 'description': 'Given the head of a singly linked list, reverse the list, and return the reversed list.', 'link': 'https://leetcode.com/problems/reverse-linked-list/', 'frequency': 4}, {'title': 'Valid Parentheses', 'description': "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.", 'link': 'https://leetcode.com/problems/valid-parentheses/', 'frequency': 3}, {'title': 'Merge Intervals', 'description': 'Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.', 'link': 'https://leetcode.com/problems/merge-intervals/', 'frequency': 2}, {'title': 'Binary Tree Inorder Traversal', 'description': "Given the root of a binary tree, return the inorder traversal of its nodes' values.", 'link': 'https://leetcode.com/problems/binary-tree-inorder-traversal/', 'frequency': 1}]

        context={
            "problems": problem_lst,
        }
        return render(request,'RevisionApp/problem_list.html#problemsComponent',context=context)
    

class SolvedView(View):
    def post(self,request):
        problem = request.POST.get('problem')
        print(problem )
        try:
            title = problem.get('title')
            description = problem.get('description')
            link = problem.get('link')
            frequency = problem.get('frequency')
            user = request.user
            Solved.objects.create(user=user,title=title,description=description,link=link,frequency=frequency)
            return JsonResponse({'message':'Problem successfully marked as solved!'},status=200)
        except Exception:
            return JsonResponse({'message':'Can\'t be marked as solved!'},status=403)
        
