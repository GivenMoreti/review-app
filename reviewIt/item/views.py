from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm



def home(request):
    items = Item.objects.all()
    context = {"items":items}
    return render(request,"item/index.html",context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = ItemForm()
    return render(request, 'item/create_item.html', {'form': form})