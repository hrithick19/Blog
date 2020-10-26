from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import kavithai,kadhai,katturai
from  django.core.paginator import Paginator


# Create your views here.
def kavithai_page(request):
    template="Post/kavithai.html"
    kavi=kavithai.objects.order_by('-pub_date')
    recent=[ obj for obj in kavi if obj.was_published_recently() ]
    paginator = Paginator(kavi, 4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    nav=["","","active",""]
    context={'kavithai':kavi,'recent':recent,'page_obj':page_obj,'nav':nav}
    return render(request,template,context)

def kathai_page(request):
    template="Post/kathai.html"
    kathai=kadhai.objects.order_by('-pub_date')
    recent=[ obj for obj in kathai if obj.was_published_recently() ]
    nav=["","","active",""]
    context={'kathai':kathai,'recent':recent,'nav':nav}
    return render(request,template,context)

def katturai_page(request):
    template="Post/katturai.html"
    katt=katturai.objects.order_by('-pub_date')
    recent=[obj for obj in katt if obj.was_published_recently()]
    nav=["","","active",""]   
    context={'katturais':katt,'recent':recent,'nav':nav}
    return render(request,template,context)

def full_katturai(request,katturai_id):
    katt = get_object_or_404(katturai, pk=katturai_id)
    nav=["","","active",""]   
    context={'katt':katt,'nav':nav}
    template="Post/full_katturai.html"
    return render(request,template,context)