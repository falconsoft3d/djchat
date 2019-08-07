from django.conf.urls import url
from ..dashboard.views import index_dashboard, login_user, auth, logout_user


urlpatterns = [
    url(r'^$', index_dashboard),
    url(r'^login$', login_user),
    url(r'^logout$', logout_user),
    url(r'^auth$', auth),
]