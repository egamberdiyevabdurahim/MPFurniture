from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms import ContactUsModelForm


def home_page_view(request):
    return render(request, 'home.html')


def contact_page_view(request):
    return render(request, 'contact.html')


class ContactPageView(CreateView):
    template_name = 'contact.html'
    form_class = ContactUsModelForm
    success_url = reverse_lazy("common:home")
