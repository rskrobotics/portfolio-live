from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    topic = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_email(self):
        send_mail(
            self.cleaned_data['topic'],
            self.cleaned_data['message'],
            settings.EMAIL_HOST_USER,
            ['krzychu1232@gmail.com'],
            fail_silently=False
        )
