from django.contrib import admin
from .models import Department, RequestExpenses, RequestHeader, AuditLog
# Register your models here.

from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json


admin.site.register(Department)
admin.site.register(RequestHeader)
admin.site.register(RequestExpenses)


@admin.register(AuditLog)
class NewStatsAuditAdmin(admin.ModelAdmin):
    def audit_stat_view(self, request,extra_context=None):
        audit_stat=(
            AuditLog.objects.filter(operating_system='Windows').count()
        )
        as_json =json.dumps(list(audit_stat), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data" :as_json}
        return super().audit_stat_view(request,extra_context=extra_context)