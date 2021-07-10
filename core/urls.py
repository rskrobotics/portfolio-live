from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static


app_name = 'core'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('skills', views.skillsView, name='skills'),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>', views.ProjectDetailView.as_view(),
         name='single_project'),
    path('thanks', views.ThanksView.as_view(), name='thanks'),
    path('contact', views.ContactFormView.as_view(), name='contact'),
]




