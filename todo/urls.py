from django.conf.urls import url

from todo.views import todoadd,todoedit,todolist,about,contact,tododelete

urlpatterns=[
    # urlbar name , function name , html page name
    url(r'^$',todolist,name='todolist'),
    url(r'^add/$',todoadd,name='todoadd'),
    # url(r'^home/$',home,name='home'),
    url(r'^contact/$',contact,name='contact'),
    # url(r'^edit/(?P<pk>\d+)/$',todoedit,name='todoedit'),
    # url(r'^delete/(?P<pk>\d+)/$',tododelete,name='tododelete'),
    
    
    url(r'^about/$',about,name='about'),
    url(r'^edit/(?P<pk>\d+)/$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)/$',tododelete,name='tododelete'),


]
# • ^ for the beginning of a text
# • $ for the ending of a text
# • \d for a digit 
# • + to inform the previous item should be repeated at least once(kam se kam ek br to wo data hona chahiye)
# • ()to capture part of a pattern
# • ? zero or one of the previous expression (zero ya 1 means ya to data h ya nahi hai)
# • * zero or more of the previous expression
# "P" path k liye likha jata hai
# pk is the primary key of database