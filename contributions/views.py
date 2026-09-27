from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Contribution
from .forms import ContributionForm
from members.models import Member
from django.db import models
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required

class ContributionListView(LoginRequiredMixin, generic.ListView):
    model = Contribution
    template_name = 'contributions/contribution_list.html'
    context_object_name = 'contributions'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Contribution.objects.select_related('giver').all()
        try:
            member = Member.objects.get(user=user)
            return Contribution.objects.filter(giver=member)
        except Member.DoesNotExist:
            return Contribution.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_staff:
            context['total_contributions'] = Contribution.objects.all().aggregate(total=models.Sum('amount'))['total']
        else:
            try:
                member = Member.objects.get(user=user)
                context['total_contributions'] = Contribution.objects.filter(giver=member).aggregate(total=models.Sum('amount'))['total']
            except Member.DoesNotExist:
                context['total_contributions'] = 0
        return context


from django.shortcuts import redirect


class ContributionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Contribution
    form_class = ContributionForm
    template_name = 'contributions/contribution_form.html'
    success_url = reverse_lazy('contributions:list')

    def form_valid(self, form):
        user = self.request.user
        try:
            member = Member.objects.get(user=user)
            form.instance.giver = member
        except Member.DoesNotExist:
            form.add_error(None, "You are not linked to a member account.")
            return self.form_invalid(form)

        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        # Debug helper to show errors if form doesn’t save
        print("Form errors:", form.errors)
        return render(self.request, self.template_name, {'form': form})

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Contribution
from django.contrib.auth.decorators import login_required

@login_required
def generate_receipt(request, contribution_id):
    if request.user.is_staff:
       contribution = get_object_or_404(Contribution, id=contribution_id)
    else:
       contribution = get_object_or_404(Contribution, id=contribution_id, giver=request.user.member)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{contribution.id}.pdf"'

    p = canvas.Canvas(response)
    p.setTitle("Contribution Receipt")

    # Header
    p.setFont("Helvetica-Bold", 18)
    p.drawString(200, 800, "ABC Church Contribution Receipt")

    # Body
    p.setFont("Helvetica", 12)
    p.drawString(50, 750, f"Member Name: {contribution.giver.full_name}")
    p.drawString(50, 730, f"Amount: Ksh {contribution.amount}")
    p.drawString(50, 710, f"Payment Method: {contribution.payment_method}")
    p.drawString(50, 690, f"Date: {contribution.date.strftime('%Y-%m-%d %H:%M')}")
    if contribution.mpesa_transaction_code:
        p.drawString(50, 670, f"M-Pesa Transaction Code: {contribution.mpesa_transaction_code}")

    p.drawString(50, 640, "Thank you for your generous contribution!")
    p.line(50, 630, 550, 630)

    # Footer
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(200, 610, "ABC Church | Faith • Service • Unity")

    p.showPage()
    p.save()

    return response

