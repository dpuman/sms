from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class MyHome(TemplateView):
    template_name = "ngo/home.html"


class About(TemplateView):
    template_name = "ngo/about.html"


class DonorPartnership(TemplateView):
    template_name = "ngo/donor-partnership.html"


class Projects(TemplateView):
    template_name = "ngo/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # for Dynamic url argument value
        type = kwargs
        myType = context["type"]

        return context


class ProjectDetails(TemplateView):
    template_name = "ngo/projects-details.html"
