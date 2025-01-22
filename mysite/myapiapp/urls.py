from django.urls import path
from .views import hello_world_view, GroupsListView

app_name = "myapiapp"

urlpatterns = [
    path('hello-api', hello_world_view, name='hello-api'),
    path('groups/', GroupsListView.as_view(), name='groups'),

]