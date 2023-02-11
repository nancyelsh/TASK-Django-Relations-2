from django.shortcuts import redirect, render

from items.forms import ItemForm
from .models import Item, Comment

# Create your views here.
def get_items(req):
    items = Item.objects.all()
    _items = []
    for item in items:
        _items.append(
            {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "image": item.image,
                "category": item.category
            }
        )
    context = {"items": _items}
    return render(req, "item_list.html", context)

def get_item(req, item_id):
    item = Item.objects.get(id=item_id)
    comments = list(item.comments.all())
    context = {
            "item": { 
                    "id": item.id,
                    "name": item.name,
                    "price": item.price,
                    "image": item.image,
                    "category": item.category,
                    "comments": comments
                }
            }
    return render(req, "item_detail.html", context)


def create_item(req):
    form = ItemForm()
    if req.method == "POST":
        form = ItemForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    context = {"form": form}
    return render(req, "item_create.html", context)