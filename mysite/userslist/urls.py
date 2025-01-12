from django.urls import path
from .views import user_form, handle_file_upload

app_name = 'userslist'

urlpatterns = [
    path('form/', user_form, name='user-form'),
    path('upload/', handle_file_upload, name='file-upload'),
]