from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Announcement

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'
    ordering = ['-created_at']

class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'
    context_object_name = 'announcement'

class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'is_public']
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcements:announcement_list')

    def test_func(self):
        return self.request.user.is_staff  # Only admin

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'is_public']
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcements:announcement_list')

    def test_func(self):
        return self.request.user.is_staff

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    template_name = 'announcements/announcement_confirm_delete.html'
    success_url = reverse_lazy('announcements:announcement_list')

    def test_func(self):
        return self.request.user.is_staff


# Create your views here.
