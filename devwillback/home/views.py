from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AboutView(TemplateView):
    template_name = "index.html"


class ResumeView(TemplateView):
    template_name = "resume.html"



class ContactView(TemplateView):
    template_name = "contact.html"


class ProjectsView(TemplateView):
    template_name = "projects.html"