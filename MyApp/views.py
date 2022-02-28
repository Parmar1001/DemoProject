from django.shortcuts import render
from MyApp.forms import SignUpForm,CustomerForm,TransferForm,RequestForm
from django.http import HttpResponseRedirect
from MyApp.models import Customer,Notification
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
def home_view(request):
    return render(request, 'MyApp/home.html')
    
def signup_view(request):
    if request.method=='POST':
       signupform=SignUpForm(request.POST)
       customerform=CustomerForm(request.POST,request.FILES)
       if signupform.is_valid() :
           user=signupform.save()
           user.set_password(user.password)
           if customerform.is_valid():
               customerinfo=customerform.save(commit=False)
               customerinfo.phonenum=user.username
               customerinfo.user_name=user
               customerinfo.save()
               user.save()
               return HttpResponseRedirect(reverse('login'))
    signupform=SignUpForm()
    customerform=CustomerForm()

    mydict={'signupform':signupform,'customerform':customerform}
    return render(request,'MyApp/sign_up.html',context=mydict)
    

@login_required
def customerInfo(request):
    show_bal=False
    current_user=request.user
    customer=Customer.objects.get(user_name_id=current_user.id)
    if request.method=='POST': 
            show_bal=True
    return render(request,'MyApp/cust_info.html',{'customer':customer,'current_user':current_user,'show_bal':show_bal})

@login_required
def transfer_view(request):
    return render(request,'MyApp/transfer.html')

@login_required
def requestMoney_view(request):
    return render(request,'MyApp/requestMoney.html')
        
           
