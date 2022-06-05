from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm


class AccountsLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountsLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = '/'


class AccountsSignupView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        valid = super(AccountsSignupView, self).form_valid(form)
        raw_password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return valid
