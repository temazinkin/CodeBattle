from django.conf.urls import url
from django.urls import (
    path,
    include
)

from account.views import (
    github_login,
    profile_page,
)

urlpatterns = [
    path('accounts/profile/', profile_page, name='profile'),
    path('', github_login, name='index'),
    url('', include('social_django.urls', namespace='social')),
]
