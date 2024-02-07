from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv

CONTENT = []
with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        CONTENT.append({
            'Name': row.get('Name'),
            'Street': row.get('Street'),
            'District': row.get('District')
        })

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    paginator = Paginator(CONTENT, 10)
    current_number_page = request.GET.get('page', 1)
    page = paginator.get_page(current_number_page)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, template_name='stations/index.html', context=context)


