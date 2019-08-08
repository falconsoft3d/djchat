from django.conf.urls import url
from ..dashboard.views import index_dashboard, login_user, auth, logout_user, dashboard_home, dashboard_register


urlpatterns = [
    url(r'^$', index_dashboard),
    url(r'^login$', login_user),
    url(r'^logout$', logout_user),
    url(r'^auth$', auth),
    url(r'^home$', dashboard_home),
    url(r'^register$', dashboard_register),
]