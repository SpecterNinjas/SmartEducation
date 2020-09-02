from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

app_name = 'registration'

urlpatterns = [
    path('password_reset/', PasswordResetView.as_view(success_url='/registration/password_reset_done'),
         name='password_reset'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(success_url='/registration/password_reset_complete'),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
