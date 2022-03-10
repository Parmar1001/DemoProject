from django.shortcuts import render, get_object_or_404
from MyApp.forms import TransferForm, RequestForm #SignupForm
from django.http import HttpResponseRedirect
from MyApp.models import Customer, Notification
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
# from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# from .tasks import send_email
# import redis


# Create your views here.
def home_view(request):
    return render(request, "MyApp/home.html")


def profile_view(request):
    return render(request, "MyApp/profile.html")


# def signup_view(request):
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
#     import pdb;pdb.set_trace()
#     mydict={'signupform':signupform,'customerform':customerform}
#     return render(request,'signup.html',context=mydict)


class ProfileView(CreateView):
    model = Customer
    template_name = "MyApp/profile.html"
    success_url = reverse_lazy('Home')
    fields = [
        "profile_pic",
        "phonenum",
        "balance",
        "account_type",
        "state",
        "city",
        "branch_name",
    ]

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(ProfileView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        initial['phonenum'] = self.request.user.username
        return initial

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(ProfileView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        customer_id = self.model.objects.get(user_id=self.request.user.pk).pk
        return reverse("customer_info", kwargs={"pk": customer_id})


# class UpdateProfileView(UpdateView):
#     model = Customer
#     template_name = "MyApp/update_profile.html"
#     fields = [
#         "profile_pic",
#         "balance",
#         "phonenum",
#         "account_type",
#         "state",
#         "city",
#         "branch_name",
#     ]
#     success_url = reverse_lazy('Home')

#     def update_profile(request, pk):
#         import pdb;pdb.set_trace()
#         profile = get_object_or_404(Customer, id=pk)


@login_required
def CustomerInfo(request,pk):
    # import pdb;pdb.set_trace()
    show_bal=False
    current_user=request.user
    # import pdb;pdb.set_trace()
    customer=Customer.objects.get(customer_id=pk)
    if request.method=='POST':
            show_bal=True
    return render(request,'MyApp/cust_info.html',{'customer':customer,'current_user':current_user,'show_bal':show_bal})


@login_required
def TransferView(request):
    msg = ""
    noti_count = Notification.objects.filter(user_id=request.user.id).count()
    if request.method == "POST":
        pin = request.POST["pin"]
        if request.user.check_password(pin):
            toAccount = request.POST["accno"]
            amount = float(request.POST["amount"])
            ProfileView = Customer.objects.get(user_id=request.user.id)
            # import pdb;pdb.set_trace()
            customerTo = Customer.objects.get(phonenum=toAccount)
            if ProfileView.balance > amount:
                ProfileView.balance = ProfileView.balance - amount
                customerTo.balance = customerTo.balance + amount
                ProfileView.save()
                customerTo.save()
                createNotificationFrom = (
                    "{}/- has been debited from your account {} on {}. ".format(
                        amount, ProfileView.phonenum, date.today()
                    )
                )
                createNotificationTo = (
                    "{}/- has been credited to you account by {} on {}. ".format(
                        amount, ProfileView.phonenum, date.today()
                    )
                )
                notificationFrom = Notification(
                    user=request.user, notification=createNotificationFrom
                )
                notificationTo = Notification(
                    user=customerTo.user, notification=createNotificationTo
                )
                notificationTo.save()
                notificationFrom.save()
                noti_count = noti_count + 1
                msg = "Transfered"
            else:
                msg = "Insufficent amount"
        else:
            msg = "Invalid pass"
        #     redis_host = redis.Redis(host="localhost", db=0)
        #     redis.set
        # send_email.delay()
    form = TransferForm()
    return render(
        request,
        "MyApp/transfer.html",
        {"form": form, "msg": msg, "noti_count": noti_count},
    )


@login_required
def RequestMoneyView(request):
    msg = ""
    noti_count = Notification.objects.filter(user_id=request.user.id).count()
    if request.method == "POST":
        toAccno = request.POST["accno"]
        reqAmount = request.POST["amount"]
        epin = request.POST["pin"]
        if request.user.check_password(epin):
            reqTo = Customer.objects.get(phonenum=toAccno)
            reqFrom = Customer.objects.get(user_id=request.user)
            createNotificationTo = "{} has requested rupees {}/- on {}".format(
                reqFrom.phonenum, reqAmount, date.today()
            )
            createNotificationToMe = "{}/- has been requested from {} on {}".format(
                reqAmount, reqTo.phonenum, date.today()
            )
            notificationTo = Notification(
                user=reqTo.user,
                 notification=createNotificationTo
            )
            notificationToMe = Notification(
                user=reqFrom.user, notification=createNotificationToMe
            )
            notificationTo.save()
            notificationToMe.save()
            noti_count = noti_count + 1
            msg = "request sent"
    form = RequestForm()
    return render(
        request,
        "MyApp/requestMoney.html",
        {"form": form, "msg": msg, "noti_count": noti_count},
    )

# def SendEmail(request):
#     # Send mail synchronously
#     #send_email()
#     # Send email asynchronously.
#     send_email.delay()
#     return render(request,)

@login_required
def NotificationView(request):
    notifications = Notification.objects.filter(user=request.user)
    if request.method == "POST":
        notifications.delete()
    return render(
        request,
        "MyApp/see_notification.html",
        {"notifications": notifications, "noti_count": notifications.count()},
    )


# class contactView(SuccessMessageMixin,CreateView):
#     model = Contact
#     template_name = 'MyApp/contact.html'
#     fields = ['full_name','email','message','date']
#     success_url = reverse_lazy('Home')
#     success_message = 'Thanks For Contact Us..!!'

#     def form_valid(self, form):
#         form.save()
#         return super(contactView,self).form_valid(form)


def ClientsView(request):
    return render(request, "MyApp/clients.html")


def AboutView(request):
    return render(request, "MyApp/about.html")


def ServiceView(request):
    return render(request, "MyApp/service.html")
