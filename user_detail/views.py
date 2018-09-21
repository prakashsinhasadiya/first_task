from django.views import View
from django.shortcuts import render
from user_detail.forms import UserDetailsForm
# Create your views here.


class UserDetail(View):

    def get(self, request):
        form = UserDetailsForm()
        import pdb; pdb.set_trace()
        return render(request, 'userdetails/home.html', {'form': form})
