from django.urls import path

from . import views

app_name = 'research'
urlpatterns = [
    path('conversions/', views.test_view),
    path('conversions/<slug:pk>/progress/',
         views.progress_view, name='progress'),
    path('conversions/<slug:pk>/',
         views.detail_view, name='status'),
]
