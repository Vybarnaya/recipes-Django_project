from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.shortcuts import render

def user_form(request: HttpRequest):
    return render(request, 'userslist/user-form.html')


def handle_file_upload(request: HttpRequest):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        print('File uploaded', filename)
    return render(request, 'userslist/file-upload.html')