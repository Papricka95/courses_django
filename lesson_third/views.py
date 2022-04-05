import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def filter_func(request):
    array_for_sort = [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    context = {
        "name_low": "LOWER",
        "value": 10,
        "first": [1, 2, 3, 4],
        "second": [5, 6, 7, 8],
        "str": "I'm using Django",
        "date": datetime.datetime.now(),
        "empty_one": "",
        "for_sort": array_for_sort,
        "float": 32.224,
        "number": 12345678,
        "boolean_var": True,
        "name": "alex",
    }
    return render(request, "filter.html", context)


# def view(request): #old methods
#     list = [0, 232, 45, 123, 4, 53423, 54, 23]
#     template = loader.get_template('index.html')
#     context = {
#         "test": "TEXT!",
#         "list": list,
#         "name": "Alex",
#         "surname": "Jazun",
#         "coords": {
#             "x": "x coords",
#             "y": "y coords",
#         },
#     #    "list": [1, 2, 3, 4],
#     }
#     return HttpResponse(template.render(context, request)) #отрендерить template из 9строчки.


def view(request): #more new methods!!!
    list_local = [0, 232, 45, 123, 4, 53423, 54, 23]
    context = {
        "test": "TEXT!",
        "list": list_local,
        "name": "Alex",
        "surname": "Jazun",
        "coords": {
            "x": "x coords",
            "y": "y coords",
        },
        #    "list": [1, 2, 3, 4],
    }
    return render(request, 'index.html', context)



def tags_if(request):
    list_loc = [1, 2, 3, 4, 5, 6]
    var1 = "var1"
    var2 = "var2"
    var3 = "var3"
    obj = {
        'name': "Alex",
        'surname': "Parker",
    }
    context = {
        "x": "x value",
        "user": "Admin",
        "list": list_loc,
        "value": 10,
        "obj": obj,
        "var": "var1",
    }
    return render(request, 'tags_if.html', context)


def tags_for(request):
    list_local = [1, 2, 3, 4, 5, 6]
    empty_list = []
    context = {
        "list": list_local,
        "empty": empty_list,
    }
    return render(request, 'tags_for.html', context)


def check(request):
    pass


def tag_in(request):
    pass