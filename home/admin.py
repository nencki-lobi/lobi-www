from django.contrib import admin

from home.models import Research, Publication, Meeting, Photo, News, Alumni
#from django.contrib.sites.models import Site
#from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from home.models import Profile

admin.site.register(Research)
admin.site.register(Publication)
admin.site.register(Meeting)
admin.site.register(Photo)
admin.site.register(News)
admin.site.register(Alumni)
#admin.site.unregister(Group)
#admin.site.unregister(Site)

class UserProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)