from django.shortcuts import render

app_name="erros"

def handler404(request, exception):
    return render(request, "erro404.html")
