from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def hello_response(request):
    return HttpResponse("Hello django response!")


def http_redirect(request):
    return redirect("/lesson-two-response/fun1/")


def fun1(request):
    return HttpResponse("Hello redirect!")


def render_html(request):
    _html = """
    <!DOCTYPE html>
    <html>
        <head>
	    <meta charset="utf-8">
	        <title></title>
        </head>
        <body>
	        Hello, rendered html!
        </body>
    </html>
    """
    return HttpResponse(_html)


def render_template(request):
    return render(request, "main.html", {})


def form_hendler(request):
    if request.POST:
        return HttpResponse("Request is POST")
    else:
        return HttpResponse("Request is GET!")