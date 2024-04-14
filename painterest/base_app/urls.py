from django.urls import path
from . import views, signup, inscription_reussie, logout, views as auth_views


urlpatterns = [
    path("", views.test, name="main"),
    path("home/", views.home, name="homes"),
    path("signup/", views.signup, name="signup"),  # URL pattern for signup route
    path("inscription_reussie/", views.inscription_reussie, name="inscription_reussie"),  # URL pattern for confirmation page
    path("login/", views.login, name="login"),# URL pattern for 'login'
    path('password-reset-email/', auth_views.PasswordResetView.as_view(), name='password_reset-email'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("logout/", auth_views.logout_view, name="logout") # URL pattern for 'logout'
]