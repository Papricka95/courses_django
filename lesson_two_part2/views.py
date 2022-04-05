from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def blog_articles(request, a, b):
    return HttpResponse('Blog articles')


def comments(request, page_number):
    return HttpResponse('Comments')


def optional_args(request, year, foo):
    return HttpResponse('Comments %s' % foo)


def report(request, id="1"):
    return HttpResponse('report %s' % id)


def history(request, page_slug, page_id):
    return HttpResponse("History")


def edit(request, page_slug, page_id):
    return HttpResponse("edit")


def discuss(request, page_slug, page_id):
    return HttpResponse("discuss")


def permissions(request, page_slug, page_id):
    return HttpResponse("permissions")
