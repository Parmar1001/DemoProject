from django.shortcuts import render
from MyApp.forms import SignUpForm,CustomerForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request, 'MyApp/home.html')
    

def signup_view(request):
    if request.method=='POST':
       signupform=SignUpForm(request.POST)
       customerform=CustomerForm(request.POST)
       if signupform.is_valid() :
           user=signupform.save()
           if customerform.is_valid():
             user.save()
             return HttpResponseRedirect('/account/login')
            #  TO  USE reverse() function
    signupform=SignUpForm()
    customerform=CustomerForm()

    mydict={'signupform':signupform,'customerform':customerform}
    return render(request,'MyApp/sign_up.html',context=mydict)         
           
