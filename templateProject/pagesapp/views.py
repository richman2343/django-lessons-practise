from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'

class NewsPageView(TemplateView):
    template_name='news.html'

class CompanyPageView(TemplateView):
    template_name='companies.html'

class CreaterPageView(TemplateView):
    template_name='creater.html'