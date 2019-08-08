from django.conf.urls import url
from ..dashboard.views import index_dashboard, change_password, dashboard_widget, login_user, auth, logout_user, dashboard_home, dashboard_register, dashboard_visitors, dashboard_record, dashboard_profile


urlpatterns = [
    url(r'^$', index_dashboard),
    url(r'^login$', login_user),
    url(r'^logout$', logout_user),
    url(r'^auth$', auth),
    url(r'^home$', dashboard_home),
    url(r'^register$', dashboard_register),
    url(r'^visitors$', dashboard_visitors),
    url(r'^record$', dashboard_record),
    url(r'^profile$', dashboard_profile),
    url(r'^widget$', dashboard_widget),
    url(r'^change_password$', change_password),
]