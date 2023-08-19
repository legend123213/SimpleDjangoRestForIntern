from django.urls import path
from . import views


urlpatterns = [
    path("personalinfo/",views.PersonalInfo.as_view()),
    path("personal/experiance/",views.PersonExperiance.as_view()),
    path("personal/experiance/<int:id>/",views.Experiance.as_view()),
    path("personal/project/",views.PersonProject.as_view()),
    path("personal/project/<int:id>",views.Projects.as_view()),
    path("personal/skills/",views.PersonSkills.as_view()),
    path("personal/skill/<int:id>",views.Skills.as_view()),
    path("resume",views.Resume.as_view())
]
