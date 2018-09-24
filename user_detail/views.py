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
        users_details = UserProfile.objects.all()
        return render(request, 'userdetails/home.html', {'user_data': users_details,'form': form})
    def post(self,request):

        response ={}
        userdetails_form = UserDetailsForm(request.POST)
        
        if userdetails_form.is_valid():
            name = userdetails_form.cleaned_data.get('name')
            email = userdetails_form.cleaned_data.get('email')
            address = userdetails_form.cleaned_data.get('address')
            mobile = userdetails_form.cleaned_data.get('mobile')
            dob = userdetails_form.cleaned_data.get('dob')
            blood_group = userdetails_form.cleaned_data.get('blood_group')
            gender = userdetails_form.cleaned_data.get('gender')

            user,created = UserProfile.objects.get_or_create(
                        name=name,email=email,address=address,mobile=mobile,dob=dob,blood_group=blood_group,gender=gender)
            import pdb; pdb.set_trace()
            request.POST['id'] = user.id
            return JsonResponse({'status': 'success', 'response': json.dumps(request.POST)})
        else:
            return JsonResponse({'status': 'fail', 'response': json.dumps(userdetails_form.errors)})

        return render(request, 'home.html', {'form': UserDetailsForm(), 'errors': form.errors})