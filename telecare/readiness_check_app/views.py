from django.shortcuts import render


# Create your views here.
def readiness(request, page):
    page = 'readiness_check_' + page + '.html'
    args = {}
    return render(request, page, args)
