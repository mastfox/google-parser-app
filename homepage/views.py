import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import TemplateView, ListView

# from questions.models import Question
from django.shortcuts import render, get_object_or_404


def index_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            is_exists = render(request, "index.html", context={"now": datetime.datetime.now()})
            # is_exists = request.user.test_suites.filter(
            #     is_active=True
            # ).exists()
        else:
            is_exists = False
        return render(
            request,
            "index.html",
            context={
                "now": datetime.datetime.now(),
                "is_exists": is_exists
            }
        )


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


