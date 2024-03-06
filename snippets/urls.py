from django.urls import path
from .views import *


urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippets_list'),
    path('snippets/<int:pk>', SnippetDetail.as_view(), name='snippet_detail')
]