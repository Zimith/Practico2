from django.urls import path
from .views import *

app_name = 'persona'

urlpatterns = [
    path(
        'lista/',
        PersonaListView.as_view(),
        name='lista'
    ),
]