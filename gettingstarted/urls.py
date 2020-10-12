from django.urls import path, include

from django.contrib import admin

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
    path("list/", projects.views.list, name="list"),
    path("stable_detail/", projects.views.stable_detail, name="stable_detail"),
    path("db/", projects.views.db, name="db"),
    path("admin/", admin.site.urls),
]
