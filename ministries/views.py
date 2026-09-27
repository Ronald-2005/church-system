# ministries/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from .models import Ministry, MembershipRequest
from .forms import MinistryForm, JoinRequestForm
from django.contrib import messages


# Admin check helper
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# Public: list ministries
def ministry_list(request):
    ministries = Ministry.objects.all()
    # TEST: marker text
    return render(request, 'ministries/ministry_list.html', {'ministries': ministries, 'test_marker': 'MINISTRY_LIST_OK'})

# Public: detail
def ministry_detail(request, slug):
    ministry = get_object_or_404(Ministry, slug=slug)

    is_member = False
    has_pending = False

    if request.user.is_authenticated:
        is_member = ministry.members.filter(id=request.user.id).exists()
        has_pending = MembershipRequest.objects.filter(
            ministry=ministry,
            user=request.user,
            approved=False
        ).exists()

    return render(request, 'ministries/ministry_detail.html', {
        'ministry': ministry,
        'is_member': is_member,
        'has_pending': has_pending,
    })


# Admin: create
@admin_required
def ministry_create(request):
    if request.method == 'POST':
        form = MinistryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ministries:ministry_list')
    else:
        form = MinistryForm()
    return render(request, 'ministries/ministry_form.html', {'form': form, 'title': 'Add Ministry'})

# Admin: edit
@admin_required
def ministry_edit(request, pk):
    ministry = get_object_or_404(Ministry, pk=pk)
    if request.method == 'POST':
        form = MinistryForm(request.POST, instance=ministry)
        if form.is_valid():
            form.save()
            return redirect('ministries:ministry_detail', slug=ministry.slug)
    else:
        form = MinistryForm(instance=ministry)
    return render(request, 'ministries/ministry_form.html', {'form': form, 'title': 'Edit Ministry'})

# Admin: delete
@admin_required
def ministry_delete(request, pk):
    ministry = get_object_or_404(Ministry, pk=pk)
    if request.method == 'POST':
        ministry.delete()
        return redirect('ministries:ministry_list')
    return render(request, 'ministries/ministry_confirm_delete.html', {'ministry': ministry})

# Member: request to join
@login_required
def request_join_ministry(request, pk):
    ministry = get_object_or_404(Ministry, pk=pk)

    # ✅ Check if already a ministry member
    if request.user in ministry.members.all():
        return redirect('ministries:ministry_detail', slug=ministry.slug)

    # ✅ Check if already requested (pending or approved)
    existing_request = MembershipRequest.objects.filter(
        ministry=ministry,
        user=request.user
    ).first()

    if existing_request:
        return redirect('ministries:ministry_detail', slug=ministry.slug)

    # ✅ Process new join request
    if request.method == 'POST':
        form = JoinRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.ministry = ministry
            req.approved = False
            req.save()
            return redirect('ministries:ministry_detail', slug=ministry.slug)

    return redirect('ministries:ministry_detail', slug=ministry.slug)


# Admin: approve join request (simple approve -> adds user to members)
@admin_required
def approve_request(request, req_pk):
    req = get_object_or_404(MembershipRequest, pk=req_pk)
    req.approved = True
    req.save()
    # add user to ministry members
    req.ministry.members.add(req.user)
    messages.success(request, f"{req.user.username} approved to join {req.ministry.name} ✅")
    return redirect('ministries:ministry_detail', slug=req.ministry.slug)

@admin_required
def pending_requests(request):
    pending = MembershipRequest.objects.filter(approved=False)
    return render(request, 'ministries/pending_requests.html', {'pending': pending})


@admin_required
def reject_request(request, req_pk):
    req = get_object_or_404(MembershipRequest, pk=req_pk)
    req.delete()
    messages.error(request, "Join request rejected ❌")
    return redirect('ministries:pending_requests')


# TEST: views importable and URLs will map to them


# Create your views here.
