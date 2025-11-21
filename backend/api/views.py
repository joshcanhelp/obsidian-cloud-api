from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Vault, ApiKey, Action

from django.utils import timezone

# TODO: Switch this to class-based views
# https://docs.djangoproject.com/en/dev/topics/class-based-views/

def root(request):
    return JsonResponse({"hi": True})

def userRegistration(request):
    user_list = list(User.objects.all().values())
    # I wonder if I can extend JsonReponse for all the output boilerplate ...
    return JsonResponse(user_list, safe=False, json_dumps_params={"indent": 2})


# Views that need authentication
def vaultList(request):
    all_vaults = Vault.objects.filter(is_active__exact=True)
    vault_list = list(all_vaults.values("id", "name", "created_utc_s", "user_id"))
    return JsonResponse(vault_list, safe=False)


def keyList(request):
    all_keys = ApiKey.objects.all()
    keys_list = list(
        all_keys.values("key", "created_utc_s", "expiration_utc_s", "vault_id")
    )
    return_list = []
    for orig_key in keys_list:
        return_list.append(
            {
                "vault_id": orig_key["vault_id"],
                "created_utc_s": orig_key["created_utc_s"],
                "active": orig_key["expiration_utc_s"] > timezone.now(),
                "key": orig_key["key"][:3] + "***",
            }
        )
    return JsonResponse(return_list, safe=False, json_dumps_params={"indent": 2})

def actionList(request):
    all_actions = Action.objects.order_by("created_utc_s").values(
        "type", "created_utc_s", "status", "path"
    )
    action_list = list(
        all_actions.values("type", "vault", "created_utc_s", "status", "path")
    )
    return JsonResponse(action_list, safe=False, json_dumps_params={"indent": 2})