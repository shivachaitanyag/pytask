from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('pytask.profile.views',
  url(r'^view/$', 'view_profile', name='view_profile'),
  url(r'^view/(?P<user_id>\d+)$', 'view_profile',
    name='view_user_profile'),
  url(r'^edit/$', 'edit_profile', name='edit_profile'),
  url(r'^notification/browse/$', 'browse_notifications',
      name='browse_notifications'),
  url(r'^notification/view/(?P<notification_id>\d+)$',
      'view_notification', name='view_notification'),
  url(r'^notification/delete/(?P<notification_id>\d+)$',
      'delete_notification', name='delete_notification'),
  url(r'^notification/unread/(?P<notification_id>\d+)$',
      'unread_notification', name='unread_notification'),
  url(r'^user/view/(?P<user_id>\d+)$', 'view_user',
      name='view_user'),
  url(r'^login/proceed$', 'login_proceed', name='login_proceed'),
)
