from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ceremony
from django.contrib import messages

class CeremonyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Ceremony
    fields = ['member', 'ceremony_type', 'date', 'location', 'officiated_by', 'notes']
    template_name = 'ceremonies/ceremony_form.html'
    success_url = reverse_lazy('ceremonies:ceremony_list')

    def form_valid(self, form):
        messages.success(self.request, "Ceremony added successfully ✅")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class CeremonyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ceremony
    fields = ['member', 'ceremony_type', 'date', 'location', 'officiated_by', 'notes']
    template_name = 'ceremonies/ceremony_form.html'
    success_url = reverse_lazy('ceremonies:ceremony_list')

    def form_valid(self, form):
        messages.success(self.request, "Ceremony updated successfully ✍️")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser



# Members and admin can view ceremonies
class CeremonyListView(LoginRequiredMixin, ListView):
    model = Ceremony
    template_name = 'ceremonies/ceremony_list.html'
    context_object_name = 'ceremonies'
    ordering = ['-date']

    def get_queryset(self):
        # Admins see all ceremonies
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Ceremony.objects.all().order_by('-date')
        # Members should also see all ceremonies (not filtered by user)
        return Ceremony.objects.all().order_by('-date')



class CeremonyDetailView(LoginRequiredMixin, DetailView):
    model = Ceremony
    template_name = 'ceremonies/ceremony_detail.html'
    context_object_name = 'ceremony'

class CeremonyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ceremony
    fields = ['ceremony_type', 'date', 'location', 'officiated_by', 'notes']
    template_name = 'ceremonies/ceremony_form.html'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, "Ceremony updated successfully ✅")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ceremonies:ceremony_list')


class CeremonyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ceremony
    success_url = reverse_lazy('ceremonies:ceremony_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Ceremony deleted ❌")
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


