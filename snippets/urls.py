from django.urls import path
from .views import *


urlpatterns = [
    path('snippets/', snippet_list, name='snippets_list'),
    path('snippets/<int:pk>', snippet_detail, name='snippet_detail')
]