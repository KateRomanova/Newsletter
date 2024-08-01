from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail.models import Newsletter


def home(request):
    return render(request, 'home.html')


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = '__all__'
    success_url = reverse_lazy('mail:newsletter_list')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = '__all__'
    success_url = reverse_lazy('mail:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mail:newsletter_list')
