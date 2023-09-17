from django.urls import path
from . import views
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path("personalinfo/",views.PersonalInfo.as_view(),name = 'personal-profile'),
    path("personal/experiances/",views.PersonExperiance.as_view(),name='personal-experiance'),
    path("personal/experiance/<int:id>/",views.Experiance.as_view(),name='individual-personal-experiance'),
    path("personal/projects/",views.PersonProject.as_view(),name='personal-projects'),
    path("personal/project/<int:id>",views.Projects.as_view(),name='person-project'),
    path("personal/skills/",views.PersonSkills.as_view(),name='personal-skills'),
    path("personal/skill/<int:id>",views.Skills.as_view(),name='personal-skill'),
    path("register/",views.Register.as_view(),name = 'user-register'),
    path("resume/",views.Resume.as_view()),
     path("login/",views.LoginUser.as_view(),name = 'user-register'),
     path("personal/educations/",views.Educations.as_view(),name='personal-educations'),
     path("personal/education/<int:id>",views.Educationpersonal.as_view(),name='personal-education'),
      path("personal/languages/",views.Personal_languages.as_view(),name='personal-educations'),
     path("personal/language/<int:id>",views.Person_language.as_view(),name='personal-education'),
     path("personal/resume/download",views.Download_resume.as_view()),
     path("getit",PDFTemplateView.as_view())
]
