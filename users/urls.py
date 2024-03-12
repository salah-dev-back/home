from django.urls import path
from users.views import UsersLoginView

app_name = 'users'

urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    # path('registration/', UsersRegisterView.as_view(), name='register')
]
