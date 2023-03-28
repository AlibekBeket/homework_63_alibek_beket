from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, AccountView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/<int:pk>', AccountView.as_view(), name='account_list'),
]
