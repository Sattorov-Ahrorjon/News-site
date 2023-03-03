from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home_page')
            else:
                form = LoginForm()
                context = {
                    'form': form
                }
                messages.success(request, "User not found")
                return render(request, 'account/login.html', context=context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'account/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('home_page')


def user_register(request):
    form = UserRegistrationForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            if user_form.cleaned_data['password'] == user_form.cleaned_data['password_2']:
                new_user = user_form.save(commit=False)
                new_user.set_password(
                    user_form.cleaned_data['password']
                )
                new_user.save()
                return render(request, 'account/register_done.html')
            else:
                messages.success(request, "Passwords are not the same !!!")
                return render(request, 'account/register.html', context=context)
        else:
            messages.success(request, "Such a user has already been created !!!")
            return render(request, 'account/register.html', context=context)
    else:
        return render(request, 'account/register.html', context=context)


# class UserCreateView(CreateView):
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('login')
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password')
#
#     template_name = 'account/register.html'
#
#
# class UserCreateView2(View):
#     def post(self, request):
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password']
#             )
#             new_user.save()
#             return render(request, 'account/register_done.html')

    # def get(self, request):
    #     form = UserRegistrationForm()
    #     context = {
    #         'form': form,
    #     }
    #     return render(request, 'account/register.html', context=context)


# @login_required()
# def user_edit(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             user_form = UserEditForm(instance=request.user, data=request.POST)
#             if user_form.is_valid():
#                 user_form.save()
#                 return redirect('home_page')
#             else:
#                 user_form = UserEditForm(instance=request.user, data=request.POST)
#                 return render(request, 'account/user_edit.html', {'user_form': user_form})
#         else:
#             user_form = UserEditForm(instance=request.user, data=request.POST)
#             return render(request, 'account/user_edit.html', {'user_form': user_form})
#     else:
#         return redirect('login')


# class UserEditView(LoginRequiredMixin, View):
#     def post(self, request):
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('home_page')
#         else:
#             user_form = UserEditForm(instance=request.user, data=request.POST)
#             return render(request, 'account/user_edit.html', {'user_form': user_form})
#
#     def get(self, request):
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         return render(request, 'account/user_edit.html', {'user_form': user_form})
