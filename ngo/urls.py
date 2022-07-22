from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyHome.as_view(), name="home"),
    path("about/", views.About.as_view(), name="about"),
    path("donor-partnership/", views.DonorPartnership.as_view(),
         name="donor_partnership"),
    path("projects/<str:type>", views.Projects.as_view(),
         name="projects"),
    path("project-details/<int:pk>", views.ProjectDetails.as_view(),
         name="project_details"),

]
