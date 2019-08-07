from django.conf.urls import url
from ..dashboard.views import index_dashboard


urlpatterns = [
    url(r'^$', index_dashboard),
]