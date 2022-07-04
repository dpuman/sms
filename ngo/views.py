from django.shortcuts import render
from django.views.generic import TemplateView


class MyHome(TemplateView):
    template_name = "ngo/home.html"


class About(TemplateView):
    template_name = "ngo/about.html"
