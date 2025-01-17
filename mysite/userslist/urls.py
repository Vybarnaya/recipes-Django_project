from django.contrib.auth.views import LoginView
from django.urls import path
from .views import get_cookie_view, \
    set_cookie_view, get_session_view, \
    set_session_view, logout_view,\
    AboutMeView, RegisterView


app_name = 'userslist'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name="userslist/login.html",
                            redirect_authenticated_user=True),
         name='login'),
    path('logout/', logout_view, name='logout'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('register/', RegisterView.as_view(), name='register'),
    path('cookie/get', get_cookie_view, name='get-cookie'),
    path('cookie/set', set_cookie_view, name='set-cookie'),
    path('session/get', get_session_view, name='get-session'),
    path('session/set', set_session_view, name='set-session'),
]