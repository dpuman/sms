from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class MyHome(TemplateView):
    template_name = "ngo/home.html"
