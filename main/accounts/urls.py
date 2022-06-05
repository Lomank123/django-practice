from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.AccountsLoginView.as_view(), name='login'),
    path('logout/', views.AccountsLogoutView.as_view(), name='logout'),
    path('signup/', views.AccountsSignupView.as_view(), name='signup'),
]
