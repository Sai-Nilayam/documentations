from django.shortcuts import render

# Self added codes.
from django.http import HttpResponse
from django.http import FileResponse

# Create your views here.


def index(request):
    import os
    script_path = os.path.abspath(__file__)
    base_path_arr = script_path.split('/')
    base_path_arr = base_path_arr[0: len(base_path_arr) - 1]
    base_path = '/'.join(base_path_arr) + '/'

    # Getting POST data from the request object.
    # first_number = request.POST['first_number']
    # second_number = request.POST['second_number']

    # Getting FILE data from the request object.
    file = request.FILES['test_file']

    # Saving file to Django server.
    ext = str(file).split('.')[1]
    # Works in Django's inbuilt server. 
    # f = open('uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'wb')
    f = open(
        base_path + 'uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'wb')
    f.write(file.read())
    f.close()

    # This is very important as normally mod_wsgi takes the default Python versio
    # and specifying this will give the script the ability to use Vertual Env
    # Packages.
    # import sys
    # version = sys.version
    # path = sys.executable
    # prefix = sys.prefix

    import numpy as np

    # Response Strings.
    # return_str = 'A Response from the Djanog app.'
    # return_str = '{}, {}.'.format(first_number, second_number)
    # return_str = str(int(first_number) + int(second_number))
    # return_str = 'The file named as {} has been uploaded to the ' \
    #     'server at \'test_app/uploaded_files\'.'.format(str(file))
    # return_str = str(version) + ' ' + str(path) + ' ' + str(prefix)

    # Creating a 'FileRespose' object.
    # f = open('test_app/uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'rb')
    # return_file_response = FileResponse(f)

    # Returning the Respose.
    return HttpResponse(np.__version__)
    # return HttpResponse(return_file_response)
