from core.models import Preference
def pref(request):
    if request.user.is_authenticated:
        _preferences = Preference.objects.filter(user=request.user).last()

    else:
        _preferences = None

    return {
        'user_pref': _preferences,
    }