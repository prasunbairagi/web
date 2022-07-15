from  django.conf.urls import url
from django.contrib.auth import views as auth_views
from account.views import Signup

urlpatterns=[
    url(r'^signup/$',Signup,name='signup'),
    url(r'^login/$',auth_views.login,{'template_name':'signin.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'next_page':'home'},name='logout'),

    ]