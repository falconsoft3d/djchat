from django.conf.urls import url
from ..dashboard.views import index_dashboard, login


urlpatterns = [
    url(r'^$', index_dashboard),
    url(r'^login$', login),
]