from django.shortcuts import render
from .models import ShopItem
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def shop_item_list(request):
    items = ShopItem.objects.all()
    return render(request, 'stationary.html', {'items': items})

def help_view(request):
    return render(request, 'help.html')

def contact_view(request):
    return render(request, 'contact.html')