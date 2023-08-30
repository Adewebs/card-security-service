from django.contrib import messages
import os
import qrcode
from PIL import Image
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import ChildParents, Pupil
from django.http import JsonResponse, HttpRequest
from django.contrib.auth import get_user_model


# Create your views here.
def samplepage(request):
    page ='sample page'
    user = request.user
    pupils = ChildParents.objects.filter(email=user)
    return render(request, 'material-kit-master/sampletest.html',
                  {'pagetitle': page, 'parents':pupils})

def loggoff_parent(request):
    logout(request)
    return redirect('home')


def loginepage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    page = 'Parent Sign In'
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            parent = ChildParents.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
        parent = authenticate(request, email=email, password=password)
        if parent is not None:
            login(request, parent)
            return render(request, 'material-kit-master/dashboard.html')
        else:
            message = 'Username OR password does not exit'
            return render(request, 'material-kit-master/pages/sign-in.html',
                          {'error': message})
    return render(request, 'material-kit-master/pages/sign-in.html',
                  {'pagetitle':page})


def register_parent(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    page = 'Sign Up'
    if request.method == 'POST':
        f_name = request.POST['Fname']
        l_name = request.POST['Lname']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        try:
            parent = ChildParents.objects.get(email=email)
            if parent is not None:
                message = 'email already exist'
                return render(request, 'material-kit-master/pages/signup.html',
                              {'error': message})
        except:
            if pass1 == pass2:
                parent = ChildParents.objects.create_user(
                username=email,  # Use email as the username
                first_name=f_name,
                last_name=l_name,
                email=email,
                password=pass1)
                parent.save()
                login(request, parent)

                # #Qr generator starts
                # user = request.user  # Assuming you have authenticated user
                # qr = qrcode.QRCode(version=1, box_size=40, border=4)
                # qr.add_data("agrolearner.com")
                # qr.make(fit=True)
                # qr_image = qr.make_image(fill_color="black", back_color="white")
                #
                # # Define the path for the QR image within the parentqr folder
                # qr_image_filename = f'qr_{user.id}.png'
                # qr_image_path = os.path.join(settings.MEDIA_ROOT, 'parentsQR', qr_image_filename)
                #
                # # Save the QR image using Django's built-in methods
                # qr_image.save(qr_image_path)
                #
                # # Update the user's parentqr field
                # user.parentqr = os.path.join('parentsQR', qr_image_filename)
                # user.save()
                # #Qr code generator ends

                return render(request, 'material-kit-master/dashboard.html')
            else:
                message = 'password and confirm password not the same'
                return render(request, 'material-kit-master/pages/signup.html',
                      {'error': message})
    return render(request, 'material-kit-master/pages/signup.html',
                  {'pagetitle':page})


def home(request):
    page = 'Card Secuirty System| Home'
    return render(request, 'material-kit-master/index.html',
                  {'pagetitle':page})


def about(request):
    return render(request, 'material-kit-master/pages/author.html')


def contact(request):
    page = 'Contact US'
    return render(request, 'material-kit-master/pages/contact-us.html',
                  {'pagetitle':page})

@login_required(login_url='signin')
def profile(request):
    return render(request, 'material-kit-master/pages/profile.html')

@login_required(login_url='signin')
def parents_dashboard(request):
    page = 'Parent Dashboard'
    return render(request, 'material-kit-master/dashboard.html',
                  {'pagetitle':page})

@login_required(login_url='signin')
def editparent(request):
    page = 'Parent Dashboard'
    editinfo = ChildParents.objects.get(id=request.user.id)

    return render(request, 'material-kit-master/editparent.html',
                  {'pagetitle':page, 'editinfo': editinfo})

@login_required(login_url='signin')
def generate_and_save_qr_images(request):
    page ='Generate QRCode'
    user = request.user  #Having authenticated user
    # Retrieve all pupils associated with the user
    pupils = Pupil.objects.filter(parent=user)  # Replace with your actual relationship
    # Generate and save QR code for each pupil
    if request.method == 'POST':
        seccurityQ = request.POST['sq']
        seccurityA = request.POST['sa']
        email = request.user.email
        infosave = ChildParents.objects.get(email=email)
        infosave.picker_security_question =seccurityQ
        infosave.picker_security_answer=seccurityA
        infosave.save()
        for pupil in pupils:
            qr_data = f"Name: {pupil.first_name} {pupil.last_name}\nRegistration: {pupil.registration_number}\nClass:{pupil.student_class}\nAge: {pupil.age}\nParent link: http://127.0.0.1:8000/verification/{user.id}/"
            qr = qrcode.QRCode(version=1, box_size=40, border=4)
            qr.add_data(qr_data)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image_filename = f'{user.first_name}_{user.last_name}_{pupil.id}.png'
            qr_image_path = os.path.join(settings.MEDIA_ROOT, 'parentsQR', qr_image_filename)
            qr_image.save(qr_image_path)
            # Update pupil's QR code field if needed
            pupil.qr_code_image = os.path.join('parentsQR', qr_image_filename)
            pupil.save()
            return render(request, 'material-kit-master/dashboard.html',
                          {'pagetitle': page})

    return render(request, 'material-kit-master/pages/generateqr.html',
                  {'pagetitle': page})
@login_required(login_url='signin')
def verificationLink(request, pk):
    page = 'Parent Info'
    parentprofile = ChildParents.objects.get(id=pk)
    return render(request, 'material-kit-master/pages/verification.html',
                  {'pagetitle': page, 'parentinfo': parentprofile})

@login_required(login_url='signin')
def pickerUpdate(request):
    page = "Update Picker's Info"
    user = request.user  # Having authenticated user
    if request.method == 'POST':
        seccurityQ = request.POST['securityquestion']
        seccurityA = request.POST['securityanswer']
        pickers_name = request.POST['pname']
        pickers_number = request.POST['number']
        pickers_descript = request.POST['description']
        email = request.user.email
        infosave = ChildParents.objects.get(email=email)
        infosave.picker_security_question = seccurityQ
        infosave.picker_security_answer = seccurityA
        infosave.picker = pickers_name
        infosave.picker_number = pickers_number
        infosave.picker_description = pickers_descript
        infosave.save()

        return render(request, 'material-kit-master/dashboard.html',
                      {'pagetitle': page})
    return render(request, 'material-kit-master/pages/updatepicker.html',
                  {'pagetitle': page})