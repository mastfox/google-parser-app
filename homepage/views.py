import datetime

# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, Http404
# from django.views import View
from django.views.generic import TemplateView, ListView
from users.forms import RegistrationForm

# from questions.models import Question
from django.shortcuts import render, get_object_or_404, redirect


def index_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
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
                "is_exists": is_exists,
                "form": form
            }
        )
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            # link = user.get_verification_link
            # user.email_user(
            #     "Email confirmation",
            #     f"Please follow the <a href='{link}'>link</a>",
            #     from_email='menedgeralex@gmail.com'
            # )
            # user.verification_email_sent_at = timezone.now()
            # user.save()
            return redirect("/login/")
        else:
            return render(request, 'index.html', context={
                "now": datetime.datetime.now(),
                "form": form
            })


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


