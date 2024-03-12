from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from users.forms import UserLoginForm


class UsersLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


# class UsersRegisterView(LoginView):
#     template_name = 'users/registration.html'
