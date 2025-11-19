from django.db import models
from django.conf import settings
import uuid


class Vaults(models.Model):
    id = models.UUIDField("Vault ID", default=uuid.uuid4, primary_key=True)
    name = models.CharField("Vault name", max_length=200)
    api_key = models.CharField("API key", max_length=64)
    is_active = models.BooleanField("Is this vault active?", default=True)
    created_utc_s = models.DateTimeField(
        "Date/time for when the Vault was created",
        auto_now=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ApiKeys(models.Model):
    key = models.CharField("API key", max_length=64, unique=True, primary_key=True)
    created_utc_s = models.DateTimeField(
        "Date/time for when the API key was created",
        auto_now=True,
    )
    expiration_utc_s = models.DateTimeField(
        "Date/time for expiration time in seconds",
        auto_now=True,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vault = models.ForeignKey(Vaults, on_delete=models.CASCADE)


class Actions(models.Model):
    id = models.UUIDField("Action ID", default=uuid.uuid4, primary_key=True)
    type = models.CharField("Action type", max_length=20)
    status = models.CharField("Status of the action", max_length=20)
    path = models.CharField("ath to the file in the vault", max_length=300)
    created_utc_s = models.DateTimeField(
        "Date/time when the Action was created",
        auto_now=True,
    )
    completed_utc_s = models.DateTimeField(
        "Date/time when the Action was completed by the client",
        auto_now=True,
    )
    vault = models.ForeignKey(Vaults, on_delete=models.CASCADE)
