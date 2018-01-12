from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import HaribhaktDetailForm,KaryakarGroupForm
from django.utils import timezone
from django.contrib import messages
from attendance.models import HaribhaktDetail,KaryakarGroup
from django.contrib.auth.decorators import login_required

# Create your views here.


class HomePage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'attendance/home.html'

@login_required
def index(request):
    haribhaktdetails = HaribhaktDetail.objects.all()
    return render(request, 'attendance/index.html', {'haribhaktdetails': haribhaktdetails})

@login_required
def newHaribhakt(request):
    if request.POST:
        form = HaribhaktDetailForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.user = request.user
            if form.save():
                return redirect('/', messages.success(request, 'Detail was successfully added.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = HaribhaktDetailForm()
        return render(request, 'attendance/newHaribhakt.html', {'form':form})

@login_required
def newKaryakarGroup(request):
    if request.POST:
        form = KaryakarGroupForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.user = request.user
            if form.save():
                return redirect('/', messages.success(request, 'Detail was successfully added.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = KaryakarGroupForm()
        return render(request, 'attendance/newKaryakargroup.html', {'form':form})

class HaribhaktDetailListView(ListView):
    model = HaribhaktDetail
    list_display = ('name','mobile_no')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context