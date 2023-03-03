from .views import (
    user_login,
    user_logout,
    user_register,
    # user_edit,
    # UserCreateView,
    # UserCreateView2,
    # UserEditView,
)
from django.contrib.auth.views import (
    # LoginView,
    # LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', user_register, name='user_register'),
    # path('user-edit/', user_edit, name='user_edit')
]

# urlpatterns += (
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('signup/', UserCreateView.as_view(), name='user_register'),
#     path('signup/', UserCreateView2.as_view(), name='user_register'),
#     path('user-edit/', UserEditView.as_view(), name='user_edit'),
# )

urlpatterns += (
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
)

urlpatterns += (
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
)