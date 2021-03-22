from django.shortcuts import render


def welcome(request):
    page = 'welcome.html'
    args = {}
    return render(request, page, args)
