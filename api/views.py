from django.http import JsonResponse
from .models import Vault, ApiKey

from django.utils import timezone


def root(request):
    return JsonResponse({})


def vaultList(request):
    all_vaults = Vault.objects.filter(is_active__exact=True)
    vault_list = list(all_vaults.values("id", "name", "created_utc_s", "user_id"))
    return JsonResponse(vault_list, safe=False)


def keyList(request):
    all_keys = ApiKey.objects.all()
    keys_list = list(
        all_keys.values(
            "key", "created_utc_s", "expiration_utc_s", "user_id", "vault_id"
        )
    )
    return_list = []
    for orig_key in keys_list:
        return_list.append(
            {
                "user_id": orig_key["user_id"],
                "vault_id": orig_key["vault_id"],
                "created_utc_s": orig_key["created_utc_s"],
                "active": orig_key["expiration_utc_s"] > timezone.now(),
                "key": orig_key["key"][:3] + "***",
            }
        )

    return JsonResponse(return_list, safe=False)
