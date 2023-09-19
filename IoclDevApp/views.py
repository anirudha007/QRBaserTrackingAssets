# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import  CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# from openai import ChatCompletion
# import openai
from .  import sentOtp
# import datetime
from django.db.models.functions import Now
from datetime import datetime
from PIL import Image
import qrcode
# Create your views here.

# ====
UID1 = []
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
            

            context = {'form':form}
            return render(request, 'IoclDevApp/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'IoclDevApp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# def chatbot_view(request):
#     conversation = request.session.get('conversation', [])

#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')

#         # Define your chatbot's predefined prompts
#         prompts = []

#         # Append user input to the conversation
#         if user_input:
#             conversation.append({"role": "user", "content": user_input})

#         # Append conversation messages to prompts
#         prompts.extend(conversation)

#         # Set up and invoke the ChatGPT model
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=prompts,
#             api_key="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"
#         )
        
#         # Extract chatbot replies from the response

#         chatbot_replies = [message['message']['content'] for message in response['choices'] if message['message']['role'] == 'assistant']

#         # Append chatbot replies to the conversation
#         for reply in chatbot_replies:
#             conversation.append({"role": "assistant", "content": reply})

#         # Update the conversation in the session
#         request.session['conversation'] = conversation

#         return render(request, 'IoclDevApp/chat.html', {'user_input': user_input, 'chatbot_replies': chatbot_replies, 'conversation': conversation})
#     else:
#         request.session.clear()
#         return render(request, 'IoclDevApp/chat.html', {'conversation': conversation})


# ==
def uidcheck():
    UID1.clear()
    

#===


# @login_required(login_url='login')
# def home(request):
#     MainFeeds = MainFeed.objects.all()
#     customers = Customer.objects.all()
#     total_device = Device_Info.objects.count()
#     delivered = Device_Info.objects.filter(status="Out for delivery").count()
#     sold = Device_Info.objects.filter(status="Sold").count()

#     context = {"MainFeeds":MainFeeds,"customers":customers,"total_device":total_device,"delivered":delivered,"sold":sold}

#     return render (request, 'IoclDevApp/dashboard.html',context)

def InformationTable(request):
    print(UID1)
    return render(request,'IoclDevApp/code_generation.html')

def Landing_apge(request,pk_test):
    uidcheck()
    UID1.append(pk_test)
    context = {'UID':pk_test}
    print(context)
    return render(request,'IoclDevApp/landing_page.html',context)

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    context = {'customer':customer}
    return  render(request,'IoclDevApp/customer.html',context)

def LoginPage(request):
    contex = {}
    return render(request,'IoclDevApp/login.html',contex)

def RegisterPage(request):
    contex = {}
    return render(request,'IoclDevApp/register.html',contex)

def dataregister(request):
    if request.method == 'POST':
        phno = request.POST.get('phno')
        # Gtime = request.POST.get('Time')
        print(phno)
        # print(Gtime)
        uid = UID1[0]
        # print(uid)
        # try:
        # Dtime = datetime.now()
        sentOtp.Smsclass.send_sms_twillio(phno,uid)
        Transiction.objects.filter(uid = uid).update(OTP=uid,Ph_No=phno,Sale_date=Now(),status="Sold")
        # except:
        #     print("Exeption on sending otp")
        return redirect('/main_qr_view')
        # update Transiction model with  phno, OTP and sale datetime. 

def mainview(request):
    return render(request,'IoclDevApp/admin.html')

@login_required(login_url='login')            
def GenQrCode(request):
    if request.method == 'POST':
        Company = request.POST.get('Company')
        quentity = request.POST.get('quentity')
        quentity = int(quentity)
        for x in range(quentity):
            now = datetime.now()
            ur_no = now.strftime('%d%m%Y%H%M%S%f')[:-4]
            Uid = Company.upper()+ur_no
            Qr_data = "http://192.168.0.159:80/code/"+Company.upper()+ur_no
            filename = ur_no+".png"
            image_path = "QrImage"
            path_qr = (f"{image_path}/"+filename)
            img = qrcode.make(Qr_data)
            resized_im = img.resize((round(img.size[0]*0.1), round(img.size[1]*0.1)))
            path_qr = (f"{image_path}/"+filename)
            resized_im.save(f"{image_path}/"+filename)
            qrdata_model = Qrdatatable(CustomerName = Company,QR_Data = Qr_data,Qr_no = ur_no,uid=Uid,Imgpath=path_qr)
            qrdata_model.save()
            transac_model = Transiction(CustomerName = Company,QR_Data = Qr_data,Qr_no = ur_no,uid=Uid,status="Reserved")
            transac_model.save()
        return redirect('/')
        
    return render(request,'IoclDevApp/genarator_form.html')
        
@login_required(login_url='login')
def home(request):
    Tran_data = Qrdatatable.objects.all()
    totalpipe = Transiction.objects.count()
    sold_pipe = Transiction.objects.filter(status="Sold").count()
    context = {"MainFeeds":Tran_data,"total_pipes":totalpipe,"sold":sold_pipe}
    return render (request, 'IoclDevApp/Qr_data_table.html',context)