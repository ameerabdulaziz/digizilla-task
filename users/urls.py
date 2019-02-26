from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('login_success/', views.LoginSuccess.as_view(), name='login_success'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]
