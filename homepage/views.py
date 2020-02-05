import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render


def index_view(request):
    if request.method == 'GET':
        return render(
            request,
            "index.html",
            context={
                "now": datetime.datetime.now()
            }
        )
