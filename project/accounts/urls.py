from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('changepass/', UserChangePasswordView.as_view(), name="changepass"),
    path('send_reset_password_email/', SendPasswordResetEmailView.as_view(),
         name="send_reset_password_email"),
    path('reset_password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name="reset_password"),
]
