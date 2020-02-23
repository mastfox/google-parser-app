import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import TemplateView

from django.shortcuts import render, redirect, get_object_or_404


def dashboard_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            is_exists = render(request,
                               "dashboard.html",
                               context={
                                   "now": datetime.datetime.now(),
                               })
        else:
            is_exists = False
        return render(request,
                      "dashboard.html",
                      context={
                          "now": datetime.datetime.now(),
                          "is_exists": is_exists
                      })
    else:
        return redirect("login.html")



