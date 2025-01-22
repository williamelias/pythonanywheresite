from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path("", views.AboutView.as_view(), name="index"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("projects/", views.ProjectsView.as_view(), name="projects"),
]