from django.shortcuts import render


def install(request, page):
    page = 'install_ ' + page + '.html'
    args = {}
    return render(request, page, args)
