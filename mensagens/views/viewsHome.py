from django.shortcuts import render

app_name="viewsHome"

def home(request):
    return render(request, "core/home.html")
