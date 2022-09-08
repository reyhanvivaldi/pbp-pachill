from django.shortcuts import render

from wishlist.models import BarangWishlist

# Create your views here.

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Kak Cinoy'
}

def show_wishlist(request):
    return render(request, "wishlist.html", context)