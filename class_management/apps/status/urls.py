from django.urls import re_path
from django.utils.translation import gettext_lazy as _

from status.views import StatusApi

app_name = 'status'

urlpatterns = [
    re_path(r'^$', StatusApi.as_view(), name='app_status')
]