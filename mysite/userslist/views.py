from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from .models import Profile

class HelloView(View):
    welcome_message = _('Welcome everyone!!!')
    def get(self, request: HttpRequest):
        return HttpResponse(f"<h1>{self.welcome_message}</h1>")

class AboutMeView(TemplateView):
    template_name = 'userslist/about-me.html'
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'userslist/register.html'
    success_url = reverse_lazy('userslist:about-me')
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request,
            username=username, password=password)
        login(request=self.request, user=user)

        return response

def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('recipesapp:list')
        # else:
        #     return render(request, 'recipesapp:base.html')

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('recipesapp:list')
    else:
        return render(request, 'userslist/login.html', {'error': 'Invalid username or password'})

def logout_view(request: HttpRequest):
    logout(request)
    # return redirect('userslist:login')
    return redirect('recipesapp:list')

def set_cookie_view(request: HttpRequest):
    response = HttpResponse("Cookie set")
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response

def get_cookie_view(request: HttpRequest):
    fizz_value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {fizz_value!r}")
@permission_required("userslist:view_profile", raise_exception=True)
def set_session_view(request: HttpRequest):
    request.session['fizz'] = 'buzz'
    return HttpResponse("Session set")


def get_session_view(request: HttpRequest):
    value = request.session.get('fizz', 'default value')
    return HttpResponse(f"Session value: {value!r}")




