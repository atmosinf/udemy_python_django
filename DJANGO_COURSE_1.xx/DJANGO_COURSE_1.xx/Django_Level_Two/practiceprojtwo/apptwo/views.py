from django.shortcuts import render
from apptwo.models import User

# Create your views here.
def index(request):
    cont = {}
    return render(request,'apptwo/index.html', context=cont)

def users(request):
    webpages_list = User.objects.order_by('first_name')
    name_dict = {'user_records':webpages_list}
    return render(request,'apptwo/users.html',context=name_dict)
