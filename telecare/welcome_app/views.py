from django.shortcuts import render


def welcome(request):
    welcome_page = 'welcome.html'
    args = {}
    return render(request, welcome_page, args)
