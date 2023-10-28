from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView
from dj_rest_auth.registration.views import (
    RegisterView,
    ResendEmailVerificationView,
    VerifyEmailView,
    SocialLoginView)
from dj_rest_auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView  
)
from dj_rest_auth.jwt_auth import get_refresh_view


urlpatterns = [
    path('registration/', include('dj_rest_auth.registration.urls')),
    path("login/", views.CustomLoginView.as_view(), name="custom_login"),
    path('user/', UserDetailsView.as_view(), name='rest_user'),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="rest_password_reset_confirm"),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="rest_password_reset_confirm"),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    path('facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('twitter/', views.TwitterLogin.as_view(), name='twitter_login'),
    path('github/', views.GitHubLogin.as_view(), name='github_login'),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    path("registration/account_confirm_email/<str:key>/", views.email_confirm_redirect, name="account_confirm_email"),
    path("password/reset/confirm/<int:uid>/<str:token>/",
        views.password_reset_confirm_redirect,
        name="password_reset_confirm",
    ),     
]
