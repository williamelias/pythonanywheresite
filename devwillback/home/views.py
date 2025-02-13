from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AboutView(TemplateView):
    template_name = "index.html"


class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self, **kwargs):
        default_context = super().get_context_data(**kwargs)
        
        #TODO: Get this from database or other source
        default_context["experience_section"] = {
            "section_name": "Experience",
            "items": [
                {
                    "name": "Backend Developer",
                    "company": "Valora",
                    "location": "Rio de Janeiro, Brazil",
                    "start_date": "2022",
                    "end_date": "Present",
                    "description": "I worked focused on backend development, focusing on Python and Django.",
                    "tags": ["Python", "Django","AWS", "Redis", "Serverless","Webscraping"]
                },
                {
                    "name": "Full Stack Developer",
                    "company": "IT Confidence",
                    "location": "Remote, Brazil",
                    "start_date": "2023",
                    "end_date": "2024",
                    "description": "I worked focused on full stack development, focusing on Django template",
                    "tags": ["Python", "Django Template","Windows server","Oracle"]
                },
                {
                    "name": "Full Stack Developer",
                    "company": "Mundo Devops",
                    "location": "Remote, Brazil",
                    "start_date": "2019",
                    "end_date": "2022",
                    "description": "I work focused on backend development in python, django template, django rest, with skills in aws, redis database, postgres database and websockets",
                    "tags": ["Python", "Django Template","websockets","Payment gateaway"]
                }
            ]
        }

        return default_context

class ContactView(TemplateView):
    # template_name = "contact.html"
    template_name = "inprogress.html"


class ProjectsView(TemplateView):
    # template_name = "projects.html"
    template_name = "inprogress.html"
class InProgressView(TemplateView):
    template_name = "inprogress.html"