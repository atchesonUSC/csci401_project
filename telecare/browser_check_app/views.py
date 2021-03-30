from django.shortcuts import render


def browser_check(request, page):
    page = 'browser_check_' + page + '.html'
    args = {}
    return render(request, page, args)
