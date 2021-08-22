from django.shortcuts import render

# Self added codes.
from django.http import HttpResponse
from django.http import FileResponse

# Create your views here.


def index(request):
    # Getting POST data from the request object.
    first_number = request.POST['first_number']
    second_number = request.POST['second_number']

    # Getting FILE data from the request object.
    # file = request.FILES['test_file']

    # Saving file to Django server.
    # ext = str(file).split('.')[1]
    # f = open('test_app/uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'wb')
    # f.write(file.read())
    # f.close()

    # Response Strings.
    # return_str = 'A Response from the Djanog app.'
    # return_str = '{}, {}.'.format(first_number, second_number)
    return_str = str(int(first_number) + int(second_number))
    # return_str = 'The file named as {} has been uploaded to the ' \
    #     'server at \'test_app/uploaded_files\'.'.format(str(file))

    # Creating a 'FileRespose' object.
    # f = open('test_app/uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'rb')
    # return_file_response = FileResponse(f)

    # Returning the Respose.
    return HttpResponse(return_str)
    # return HttpResponse(return_file_response)
