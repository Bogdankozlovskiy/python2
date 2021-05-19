from django.shortcuts import render


def main_page(request):
    return render(request, "sales_manager/index.html")

