from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_item': data_item_katalog,
        'nama': 'Majid Rajendra Rahmat',
        'id': '2106752382'
    }
    return render(request, "katalog.html", context)
