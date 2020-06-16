from django.shortcuts import render
from datetime import datetime
from .models import Quote

def index(request):
    import random
    populate_db()
    quotes = get_quotes()
    context={
        'quotes':quotes,
        'current_date':datetime.now(),
        'title':'Quote Generator'
    }
    return render(request,'index.html',context)

def get_quotes():
    result=Quote.objects.distinct().order_by('author')[:5]
    return result

def populate_db():
    if Quote.objects.count() == 0:
        Quote(author='Mahatma Gandhi',content='Be the change you wish the world to see').save()