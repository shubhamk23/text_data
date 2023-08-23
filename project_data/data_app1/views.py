# https://ordinarycoders.com/blog/article/django-user-register-login-logout
# https://github.com/HamzahSikandar/Django_Login_System/tree/main
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import user_info
from .models import *
# from .forms import DocumentForm
from .forms import UploadFileForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from data_app1.download_video import Download_Video

@login_required(redirect_field_name="login.html")
# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    print("Hello Wrlcome to post")
    data = user_info.objects.all()
    print("Data:-", data)
    
    return render(request, "about.html", {'info':data})


def upload_document(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        
        username = request.POST.get('username')
        print("Username of records", username)
        # getting the file name from request method == POST and attribute as FILES
        # file = ''
        for f in request.FILES.getlist('file'):
            file = str(f)
            print(file)
            if '.mp4' not in file:
                document_obj = document_save.objects.create(document=file, username=username)
            else:
                document_obj = document_save.objects.create(video_file=file, username=username)
            document_obj.save()

        # file  =  request.FILES.getlist('file')[1]
        # Saving the document with FileField attribute in models.py (Database)
        # document_obj = document_save.objects.create(document=file)

        document_field = document_save.objects.all()
        print("All the files in database saved", document_field)

        ## document.pk means primary key which is id field
        # return HttpResponse("The name of uploaded file with id" + str(document_obj.auto_increment_id) + " has the file:- "+ str(document_obj.document))
        return render(request, 'success.html', {'data':document_field})
    else:
        form = UploadFileForm()

    return render(request, 'upload_document.html', {'form':form})

def data_text(request):
    print("It is call data text function")
    filename = "uploads/credentials.txt"
    print(request['username'])
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    return render(request, 'data_file.html', {'data':content})

def SignupPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        print("username", username)

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password is not same !! Please try again later")
        else:

            my_user= User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'signup.html')
        
def LoginPage(request):
    user = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        print("Username:-", username)
        pass1 = request.POST.get('pass')
        print("Password is ", pass1)
        user = authenticate(request, username=username, password=pass1)
        print("Authenticating:- ", user)
        if User.objects.filter(username=username, password=pass1):
            print("User already Exist, please try to login.")
            return render(request, "login.html")
        else:
            if user is not None:
                login(request, user)
                print("User authentication is successfully done")
                return redirect("home")
            else:
                return HttpResponse ("Username or Password is incorrect !!!")
    return render(request, "login.html", {'user_auth':user})

def LogoutPage(request):
    print("Calling Logout page")
    result = logout(request)
    print("Logout Successfully Done:- ", result)
    return redirect('login')


def SongHome(request):
    return render(request, "SongHome.html")

def downloadHome(request):
    return render(request, "download_video.html")


def download_video_view(request):
    # Initialize the object 
    obj1 = Download_Video()

    # getting playlist url from code
    playlist_url = ''
    if request.method == 'POST':
        playlist_url = request.POST.get('YoutubeURL')


    # Define the parameters
    # playlist_url = "https://wz1cgxiH5KCBsyQij1HsPtGww.youtube.com/playlist?list=PL0b6OzIxLPb"
    # playlist_url = "https://www.youtube.com/playlist?list=PLVBKjEIdL9bsgfTLn9AihqIKXYH8y33cS"
    save_path = "testing_video"

    # Checking the url playlist
    list_url = obj1.get_playlist_urls(playlist_url)

    print(list_url)
    # cleaning the spaces inside url
    list_url = [url.strip() for url in list_url]

    print('Number Of Videos In playlist: %s' % len(list_url))

    for index, url in enumerate(list_url):
        print(str(index+1)+") "+ url)

        # here strip is required to pass clean url
        obj1.Download(url, save_path)
    return HttpResponse("Downloading is successfully Done! Please check the saved folder for same.")


