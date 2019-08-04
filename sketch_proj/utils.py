from django.contrib.auth import logout
from django.shortcuts import redirect, reverse


def log_out(request):
    print(request.COOKIES)
    logout(request)
    return redirect(reverse('blogs_list_url'))
