from django.urls import path, include

from django.contrib import admin

#  I just added the two lines below to work with the debugger I just installed
#  as well as a line in urlpatterns.


#import debug_toolbar
from django.conf import settings




admin.autodiscover()
import projects.views



# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", projects.views.index, name="index"),
    path("daily", projects.views.daily, name="daily"),
    path("buildings_google", projects.views.buildings_google, name="buildings_google"),
    path("list/", projects.views.list, name="list"),
    path("portal/", projects.views.portal, name="portal"),
    path("stable_detail/", projects.views.stable_detail, name="stable_detail"),
    path("db/", projects.views.db, name="db"),
    path("mytest/", projects.views.mytest, name="mytest"),
    path("admin/", admin.site.urls),
    #path('__debug__/', include(debug_toolbar.urls)),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
