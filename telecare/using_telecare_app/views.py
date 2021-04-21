from django.shortcuts import render


def using_telecare(request, page):
    page = 'using_telecare_' + page + '.html'
    args = {}
    return render(request, page, args)
