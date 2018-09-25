from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render
from user_detail.forms import UserDetailsForm
from user_detail.models import UserProfile
from django.http import JsonResponse,HttpResponse
import json
from datetime import datetime


# Create your views here.


class UserDetail(View):

    def get(self, request):
        form = UserDetailsForm()
        users_details = UserProfile.objects.all()
        return render(request, 'userdetails/home.html', {'user_data': users_details,'form': form})
    
    def post(self,request):

        response ={}
        import pdb; pdb.set_trace()
        userdetails_form = UserDetailsForm(request.POST)
        
        if userdetails_form.is_valid():
            name = userdetails_form.cleaned_data.get('name')
            email = userdetails_form.cleaned_data.get('email')
            address = userdetails_form.cleaned_data.get('address')
            mobile = userdetails_form.cleaned_data.get('mobile')
            dob = userdetails_form.cleaned_data.get('dob')
            blood_group = userdetails_form.cleaned_data.get('blood_group')
            gender = userdetails_form.cleaned_data.get('gender')

            user = UserProfile.objects.create(
                        name=name,email=email,address=address,mobile=mobile,dob=dob,blood_group=blood_group,gender=gender)
            result = dict(request.POST) 
            result['id'] = user.id
            import pdb; pdb.set_trace()
            return JsonResponse({'status': 'success', 'response': json.dumps(result)})
        else:
            return JsonResponse({'status': 'fail', 'response': json.dumps(userdetails_form.errors)})

        return render(request, 'home.html', {'form': UserDetailsForm(), 'errors': form.errors})

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id= request.POST.get("id","")
        student = UserProfile.objects.filter(id=id).delete()
        import pdb;pdb.set_trace()
        return JsonResponse({'status': 'success', 'response': json.dumps(request.POST)})

@csrf_exempt
def edit(request):
    if request.method == 'POST':
        pass
        id = int(request.POST.get('default_user_id'))
        # import pdb; pdb.set_trace()
        user, created = UserProfile.objects.get_or_create(id=id)
        if not created:
            user.name = request.POST.get("name","")
            user.email = request.POST.get("email","")
            user.address = request.POST.get("address","")
            user.mobile = request.POST.get("mobile","")
            user.dob = request.POST.get("dob","")
            user.blood_group = request.POST.get("blood_group","")
            user.gender = request.POST.get("gender","")
            user.save()
            import pdb;pdb.set_trace()
            return JsonResponse({'status': 'success', 'response': json.dumps(request.POST)})
        else:
            return

        # user_detail = UserProfile.objects.filter(id=id).values()
        # user_detail[0]['id'] = request.POST.get("id","")
        # user_detail[0]['row_id'] = request.POST.get("row_id","")
        # import pdb; pdb.set_trace()
        # return JsonResponse({'status': 'success', 'response': json.dumps(user_detail[0])})
