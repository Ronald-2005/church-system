from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import RegisterForm, EditProfileForm

User = get_user_model()


# ✅ Registration
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# ✅ Login with role-based redirect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Role or Superuser-based redirect
            if user.is_superuser or getattr(user, 'role', '') == 'admin':
                return redirect('accounts:admin_profile')
            else:
                return redirect('accounts:member_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


# ✅ Logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('accounts:login')


# ✅ Member dashboard
@login_required
def member_dashboard(request):
    return render(request, 'accounts/member_dashboard.html')


# ✅ Admin check
def is_admin(user):
    return user.is_superuser or getattr(user, 'role', '') == 'admin'


# ✅ Admin profile
@login_required
@user_passes_test(is_admin)
def admin_profile(request):
    return render(request, 'accounts/admin_profile.html', {'user': request.user})


# ✅ Admin dashboard
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'accounts/admin_dashboard.html', {'users': users})


# ✅ Edit profile (same for all)
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


# ✅ Basic member profile
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
