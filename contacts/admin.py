from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","num","email","notes","createdTime"

admin.site.register(Member,MemberAdmin)
