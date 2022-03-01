from django.shortcuts import render
from MyApp.forms import SignUpForm,CustomerForm,TransferForm,RequestForm
from django.http import HttpResponseRedirect
from MyApp.models import Customer,Notification
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date



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
    msg=''
    noti_count=Notification.objects.filter(user_name_id=request.user.id).count()
    if request.method=='POST':
        pin=request.POST['pin']
        if request.user.check_password(pin):
           toAccount=request.POST['accno']
           amount=float(request.POST['amount'])
           customerFrom=Customer.objects.get(user_name_id=request.user.id)
           customerTo=Customer.objects.get(phonenum=toAccount) 
           if customerFrom.balance>amount:
               customerFrom.balance=customerFrom.balance-amount
               customerTo.balance=customerTo.balance+amount
               customerFrom.save()
               customerTo.save()
               createNotificationFrom="{}/- has been debited from your account {} on {}. ".format(amount,customerFrom.phonenum,date.today())
               createNotificationTo="{}/- has been credited to you account by {} on {}. ".format(amount,customerFrom.phonenum,date.today())
               notificationFrom=Notification(user_name=request.user,notification=createNotificationFrom)
               notificationTo=Notification(user_name=customerTo.user_name,notification=createNotificationTo)
               notificationTo.save()
               notificationFrom.save()
               noti_count=noti_count+1
               msg='Transfered'
           else:
               msg='Insufficent amount'
        else:
            msg='Invalid pass'
    form=TransferForm()
    return render(request,'MyApp/transfer.html',{'form':form,'msg':msg,'noti_count':noti_count})

@login_required
def requestMoney_view(request):
    msg=""
    noti_count=Notification.objects.filter(user_name_id=request.user.id).count()
    if request.method=='POST':
         toAccno=request.POST['accno']
         reqAmount=request.POST['amount']
         epin=request.POST['pin']
         if request.user.check_password(epin):
             reqTo=Customer.objects.get(phonenum=toAccno)
             reqFrom=Customer.objects.get(user_name=request.user)
             createNotificationTo="{} has requested rupees {}/- on {}".format(reqFrom.phonenum,reqAmount,date.today())
             createNotificationToMe="{}/- has been requested from {} on {}".format(reqAmount,reqTo.phonenum,date.today())
             notificationTo=Notification(user_name=reqTo.user_name,notification=createNotificationTo)
             notificationToMe=Notification(user_name=reqFrom.user_name,notification=createNotificationToMe)
             notificationTo.save()
             notificationToMe.save()
             noti_count=noti_count+1
             msg='request sent'
    form=RequestForm()
    return render(request,'MyApp/requestMoney.html',{'form':form,'msg':msg,'noti_count':noti_count})


@login_required
def notification_view(request):
        noti_count=Notification.objects.filter(user_name_id=request.user.id).count()
        if request.method=='POST':
           notifications=Notification.objects.filter(user_name=request.user).all()
           notifications.delete()
           noti_count=0
        else:
           notifications=Notification.objects.filter(user_name=request.user)
        return render(request,'MyApp/see_notification.html',{'notifications':notifications,'noti_count':noti_count})

def contact_view(request):
    return render(request,'MyApp/contact.html')


def clients_view(request):
    return render(request,'MyApp/clients.html')


def about_view(request):
    return render(request,'MyApp/about.html')
    

def service_view(request):
    return render(request,'MyApp/service.html')