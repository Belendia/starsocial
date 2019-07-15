from django.contrib import admin
from . import models

# Register your models here.

# this is to edit the GroupMember model inline in the Group app interface in the admin app


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
