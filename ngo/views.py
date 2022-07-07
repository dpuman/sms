from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class MyHome(TemplateView):
    template_name = "ngo/home.html"


class About(TemplateView):
    template_name = "ngo/about.html"


class DonorPartnership(TemplateView):
    template_name = "ngo/donor-partnership.html"
