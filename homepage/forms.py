from django import forms
from django.contrib.auth import get_user_model
import users.forms


def form(request):
    return render(request, context={
            "form": form
        })
