from django.views import View
from django.shortcuts import render
from user_detail.forms import UserDetailsForm
from user_detail.models import UserProfile
from django.http import JsonResponse,HttpResponse
import json

# Create your views here.


class UserDetail(View):

    def get(self, request):
        form = UserDetailsForm()
        return render(request, 'userdetails/home.html', {'form': form})
    def post(self,request):
        data ={}
        userdetails_form = UserDetailsForm(request.POST)
        if not userdetails_form.is_valid():
            data['error_message'] = userdetails_form.errors
            return JsonResponse(data)
        name = userdetails_form.cleaned_data.get('name')
        email = userdetails_form.cleaned_data.get('email')
        address = userdetails_form.cleaned_data.get('address')
        mobile = userdetails_form.cleaned_data.get('mobile')
        dob = userdetails_form.cleaned_data.get('dob')
        blood_group = userdetails_form.cleaned_data.get('blood_group')
        gender = userdetails_form.cleaned_data.get('gender')

        user,created = UserProfile.objects.get_or_create(
                    name=name,email=email,address=address,mobile=mobile,dob=dob,blood_group=blood_group,gender=gender)
        if created:
            return HttpResponse(json.dumps(request.POST.dict()), content_type="application/json")
        else:
            import pdb;pdb.set_trace()
            data['error_message'] = 'something problem in create user'
            return HttpResponse(json.dumps(data), content_type="application/json")