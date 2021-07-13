from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from .forms import ContactForm
from .models import Project


def homeView(request):
    '''View for our home page'''
    return render(request, 'core/home.html')


class ProjectsView(ListView):
    '''View for projects model'''
    model = Project

    def get_queryset(self):
        return Project.objects.all().order_by('-importance')


class ProjectDetailView(DetailView):
    '''View for projects model'''
    model = Project


class ContactFormView(FormView):
    '''View for contact form'''
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = 'thanks'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ThanksView(TemplateView):
    '''Thank you template'''
    template_name = 'core/thanks.html'
