from django.shortcuts import render
import datetime as dt

def index(request):
    date = dt.date.today()    

    return render(request, 'index.html', {"date": date, "projects":projects})