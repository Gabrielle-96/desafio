from django.shortcuts import render
from django.contrib.auth.decorators import login_required

app_name="viewsHome"

@login_required
def home(request):
    return render(request, "core/home.html")
