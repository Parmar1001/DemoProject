from django.shortcuts import render
from MyApp.forms import TransferForm,RequestForm
from django.http import HttpResponseRedirect
from MyApp.models import Customer,Notification,Contact
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
# from .forms import SignupForm
# SignUpForm,CustomerForm,



# Create your views here.
def HomeView(request):
    return render(request, 'MyApp/home.html')


class SignupForm(CreateView):
    model = Customer
    fields = ['username','password','email','first_name','last_name','profile_pic','balance','account_type','state','city','branch_name']
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account_login')
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(SignupForm, self).form_valid(form)


# def SignupView(request):
#     if request.method=='POST':
#        signupform=SignUpForm(request.POST)
#        customerform=CustomerForm(request.POST,request.FILES)
#        if signupform.is_valid() :
#            user=signupform.save()
#            user.set_password(user.password)
#            if customerform.is_valid():
#                customerinfo=customerform.save(commit=False)
#                customerinfo.phonenum=user.username
#                customerinfo.user_name=user
#                customerinfo.save()
#                user.save()
#                return HttpResponseRedirect(reverse('login'))
#     signupform=SignUpForm()
#     customerform=CustomerForm()

#     mydict={'signupform':signupform,'customerform':customerform}
#     return render(request,'MyApp/sign_up.html',context=mydict)
    

@login_required
def CustomerInfo(request):
    show_bal=False
    # customer=Customer.objects.get(user_name_id=request.user.id)
    if request.method=='POST': 
            show_bal=True
    return render(request,'MyApp/cust_info.html',{'customer':request.user.customer,'show_bal':show_bal})

@login_required
def TransferMoney(request):
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
def RequestMoney(request):
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
def NotificationView(request):
    notifications=Notification.objects.filter(user_name=request.user)
    if request.method=='POST':
        notifications.delete()
    return render(request,'MyApp/see_notification.html',{'notifications':notifications,'noti_count':notifications.count()})



class ContactView(SuccessMessageMixin,CreateView):
    model = Contact
    template_name = 'MyApp/contact.html'
    fields = ['full_name','email','message','date']
    success_url = reverse_lazy('Home')
    success_message = 'Thanks For Contact Us..!!'
    def post(self, form):
        form.save()
        return super(ContactView,self).post(form)



def ClientsView(request):
    return render(request,'MyApp/clients.html')



def AboutView(request):
    return render(request,'MyApp/about.html')



def ServiceView(request):
    return render(request,'MyApp/service.html')

