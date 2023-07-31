# https://ordinarycoders.com/blog/article/django-user-register-login-logout



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import user_info
from .models import *
# from .forms import DocumentForm
from .forms import UploadFileForm 

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    print("Hello Wrlcome to post")
    data = user_info.objects.all()
    print("Data:-", data)
    
    return render(request, "about.html", {'info':data})

# def upload_document(request):
#     print("Uploading a file")
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         print("Inside form")
#         if form.is_valid():
#             # Process the uploaded file (you can save it to the MEDIA_ROOT)
#             form.save()
#             return render(request, 'success.html', {'data':content})
#     else:
#         form = DocumentForm()
#     return render(request, 'upload_document.html', {'form': form})

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