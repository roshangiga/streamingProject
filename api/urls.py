from django.urls import path, re_path

from . import views
from .views import TitleList, TitleDetailAPIView
from rest_framework.authtoken import views as authViews


urlpatterns = [
    path('api/titles', TitleList.as_view(), name='all-titles'),
    re_path('api/titles/$', views.titles_filters, name='titles-filters'),

    path('api/title/<int:pk>', TitleDetailAPIView.as_view(), name='title-detail'),

    path('api/token/', authViews.obtain_auth_token),
]

