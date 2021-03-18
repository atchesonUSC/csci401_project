from django.shortcuts import render


def main_menu_0(request):
    menu_page = 'main_menu_0.html'
    args = {}
    return render(request, menu_page, args)
