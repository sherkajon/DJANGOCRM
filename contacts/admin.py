from django.contrib import admin
from .models import Contact, Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'designation')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Organization, OrganizationAdmin)


