from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Member
from .forms import MemberForm

# === Helper ===
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# === Dashboards ===
@admin_required
def admin_dashboard(request):
    return render(request, 'members/admin_dashboard.html')

@login_required
def member_dashboard(request):
    return render(request, 'members/member_dashboard.html')

# === Member Views ===

# List - Admin only
@admin_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

# Detail - Admin only
@admin_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})

# Create - Admin only
@admin_required
def member_create(request):
     from .models import Member
    # Prevent creating multiple profiles for one user
     if hasattr(request.user, 'member'):
        return redirect('members:member_list')
     if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
         member = form.save(commit=False)
         member.user = request.user   
        form.save()
        return redirect('members:member_list')
     else:
        form = MemberForm()
     return render(request, 'members/member_form.html', {'form': form, 'title': 'Add Member'})

# Edit - Admin only
@admin_required
def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members:member_detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/member_form.html', {'form': form, 'title': 'Edit Member'})

# Delete - Admin only
@admin_required
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('members:member_list')
    return render(request, 'members/member_confirm_delete.html', {'member': member})
