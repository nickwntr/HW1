import hashlib
import random

from django.contrib import messages
from django.core import paginator
from django.db import IntegrityError
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Max
from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import *
# Create your views here.
def start(request):
    response = redirect("/shop/")
    return response


def eshop(request):
    Prods = ProdModel.objects.all().order_by('id')
    pagin = Paginator(Prods,4)
    page_num = request.GET.get('page')
    page_obj = pagin.get_page(page_num)
    contextdict = {
        "page_obj": page_obj
    }
    return render(request,"prodlist.html",context=contextdict)


