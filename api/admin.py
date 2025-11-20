from django.contrib import admin

from .models import Vault, ApiKey, Action

admin.site.register(Vault)
admin.site.register(ApiKey)
admin.site.register(Action)