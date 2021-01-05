from django.shortcuts import render
from account.models import Account




def home(request):
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    return render(request, 'economyyethu/home.html', context)


   

   


