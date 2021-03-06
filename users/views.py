from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
    )
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.forms import EmailValidationOnForgotPassword, UserRegisterForm


class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        super(Login, self).form_valid(form)
        self.request.session['user_logged_in'] = self.request.POST.get('username')
        if self.request.is_ajax():
            data = {
                'valid': True
            }
            return JsonResponse(data)
        return super().form_valid(form)

    def form_invalid(self, form):
        super(Login, self).form_invalid(form)
        if self.request.is_ajax():
            data = {
                'valid': False,
                'error': 'Username or password are not valid!'
            }
            return JsonResponse(data)
        return super().form_invalid(form)


def register(request):
    if 'user_logged_in' in request.session or request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            login(request, user)
            request.session['user_logged_in'] = username
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class LoginSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'users/login_success.html'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class PasswordReset(PasswordResetView):
    form_class = EmailValidationOnForgotPassword
    subject_template_name = 'users/password_reset_subject.txt'
    email_template_name = 'users/password_reset_email.html'

    def get_template_names(self):
        if 'user_logged_in' in self.request.session or self.request.user.is_authenticated:
            raise PermissionDenied
        else:
            self.template_name = 'users/password_reset.html'
            return self.template_name


class PasswordResetDone(PasswordResetDoneView):

    def get_template_names(self):
        if 'user_logged_in' in self.request.session or self.request.user.is_authenticated:
            raise PermissionDenied
        else:
            self.template_name = 'users/password_reset_done.html'
            return self.template_name


class PasswordResetConfirm(PasswordResetConfirmView):
    def get_template_names(self):
        if 'user_logged_in' in self.request.session or self.request.user.is_authenticated:
            raise PermissionDenied
        else:
            self.template_name = 'users/password_reset_confirm.html'
            return self.template_name


class PasswordResetComplete(PasswordResetCompleteView):
    def get_template_names(self):
        if 'user_logged_in' in self.request.session or self.request.user.is_authenticated:
            raise PermissionDenied
        else:
            self.template_name = 'users/password_reset_complete.html'
            return self.template_name
