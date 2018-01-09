from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.utils import timezone
from attendance.models import HaribhaktDetail

# Create your views here.

class HomePage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'attendance/home.html'

class HaribhaktDetailListView(ListView):
	model = HaribhaktDetail
	list_display = ('name','mobile_no')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

# from articles.models import Article

# class ArticleListView(ListView):

#     model = Article

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context