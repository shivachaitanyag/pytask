from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pytask.taskapp.views import user as userViews
from pytask.taskapp.views import task as taskViews

from pytask.taskapp.forms.user import RegistrationFormCustom
from registration.views import register

urlpatterns = patterns('',
    # Example:
    # (r'^pytask/', include('pytask.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    (r'^$', userViews.homepage),
    
    (r'^task/browse/$', taskViews.browse_tasks),
    (r'^task/view/tid=(\d+)$', taskViews.view_task),
    (r'^task/create/$', taskViews.create_task),
    (r'^task/addmentor/tid=(\d+)', taskViews.add_mentor),
    #(r'^task/addtasks/tid=(\d+)', taskViews.add_tasks),
    (r'^task/edit/tid=(\d+)', taskViews.edit_task),
    (r'^task/claim/tid=(\d+)', taskViews.claim_task),
    (r'^task/assign/tid=(\d+)', taskViews.assign_task),
    
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/register/$',register,{'form_class' : RegistrationFormCustom},name='registration_register'),
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/profile/$', userViews.view_my_profile),
    
    (r'^user/view/uid=(\d+)$', userViews.view_my_profile),
    (r'^user/edit/?$', userViews.edit_my_profile),
    
)
