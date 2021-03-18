from django.shortcuts import render


# About USC TeleHELP
def main_menu(request, page):
    menu_page = 'main_menu_' + page + '.html'
    args = {}
    return render(request, menu_page, args)
