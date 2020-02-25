import datetime
import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import TemplateView
from django.db import migrations, models

from django.shortcuts import render, redirect, get_object_or_404
from requests_html import HTMLSession
from jboard.models import Parsers


# def jboard_view(request):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             parser_data = Parsers.objects.all()
#             return render(request, "jboard.html", {"parser_data": parser_data})
#         else:
#             is_exists = False
#         return render(request,
#                       "jboard.html",
#                       context={
#                           "now": datetime.datetime.now(),
#                           "is_exists": is_exists
#                       })
#     else:
#         return redirect("login.html")


# # получение данных из бд
def jboard_view(request):
    if request.method == 'GET':
        parser_data = Parsers.objects.all()
        return render(request, "jboard.html", {"parser_data": parser_data})
    else:
        return redirect("login.html")


def get_response(keyword, top_count):
    session = HTMLSession()

    google_url = f'https://www.google.com/search?q={keyword}&num={top_count}&hl=en'
    resp = session.get(google_url)
    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')
    text = resp.html.xpath('//div[@class="r"]/a/h3/text()')
    description = [element.text for element in resp.html.find('.st')]

    return links, text, description


def create(request):
    number = 0
    top_count = request.POST.get("count-field")
    keyword = request.POST.get("keyword")
    req = get_response(keyword, top_count)
    if request.method == "POST":
        for i in req[0]:
            result = Parsers()
            result.link = i
            result.title = req[1][number]
            result.description = req[2][number]
            result.position = number + 1
            result.update = datetime.datetime.now()
            result.save()
            number += 1
    return redirect("/jboard/")


def delete(request):
    result = Parsers.objects.all()
    result.delete()
    return redirect("/jboard/")


def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'link', 'title', 'description', 'position', 'update'])

    result = Parsers.objects.all().values_list('id', 'link', 'title', 'description', 'position', 'update')
    for data in result:
        writer.writerow(data)

    return response


