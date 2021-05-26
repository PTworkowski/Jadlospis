from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UserUpdateForm, UserProfileUpdateForm, CustomUserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, "account/login.html")




def register(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            form.save()
            messages.success(
                request,
                f"Stworzono konto dla {username}! Poczekaj na aktywację przez administrację",
            )
            return redirect("account-login")
    else:
        form = CustomUserRegisterForm
    return render(request, "account/registration.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Account has bean updated")
            return redirect("account-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "account/profile.html", context)
