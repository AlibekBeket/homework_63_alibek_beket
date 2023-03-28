from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView

from accounts.forms import LoginForm, CustomUserCreationForm

from instagram.models import Posts

from accounts.models import Account


# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('posts_list')


def logout_view(request):
    logout(request)
    return redirect('posts_list')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST.get('avatar'))
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class AccountView(ListView):
    template_name = 'user_detail.html'
    model = Posts
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = get_object_or_404(Account, pk=self.kwargs['pk'])
        return context

