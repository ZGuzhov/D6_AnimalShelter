from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from pets.models import Animal

class PetListView(ListView):

    model = Animal
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        context = super().get_queryset()
        get_params = self.request.GET.dict()

        if get_params.get('search'):
            context = context.filter(name__icontains=get_params.get('search'))

        return context


class AnimalView(DetailView):

    model = Animal


class ContactsView(TemplateView):

    template_name = 'contacts.html'


class AboutView(TemplateView):

    template_name = 'about.html'