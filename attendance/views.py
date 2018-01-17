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
def editHaribhaktDetail(request, haribhaktdetail_id):
    haribhakt = HaribhaktDetail.objects.get(id=haribhaktdetail_id)
    if request.POST:
        form = HaribhaktDetailForm(request.POST, instance=haribhakt)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'HaribhaktDetail was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = HaribhaktDetailForm(instance=haribhakt)
        return render(request, 'attendance/editHaribhakt.html', {'form': form})


@login_required
def deleteHaribhaktDetail(request, haribhaktdetail_id):
    haribhakt = HaribhaktDetail.objects.get(id=haribhaktdetail_id)
    haribhakt.delete()
    return redirect('/', messages.success(request, 'Details was successfully deleted.', 'alert-success'))


@login_required
def newKaryakarGroup(request):
    if request.POST:
        form = KaryakarGroupForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/attendance/karyakargroups/', messages.success(request, 'Detail was successfully added.', 'alert-success'))
            else:
                return redirect('/attendance/karyakargroup/new', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/attendance/karyakargroup/new', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = KaryakarGroupForm()
        return render(request, 'attendance/newKaryakargroup.html', {'form':form})

@login_required
def editKaryakarGroup(request, karyakargroup_id):
    karyakar = KaryakarGroup.objects.get(id=karyakargroup_id)
    if request.POST:
        form = KaryakarGroupForm(request.POST, instance=karyakar)
        if form.is_valid():
            if form.save():
                return redirect('/attendance/karyakargroups/', messages.success(request, 'KaryakarGroup was successfully updated.', 'alert-success'))
            else:
                return redirect('/attendance/karyakargroup/edit', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/attendance/karyakargroup/edit', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = KaryakarGroupForm(instance=karyakar)
        return render(request, 'attendance/editKaryakargroup.html', {'form':form})

@login_required
def deleteKaryakarGroup(request, karyakargroup_id):
    karyakar = KaryakarGroup.objects.get(id=karyakargroup_id)
    karyakar.delete()
    return redirect('/attendance/karyakargroups/', messages.success(request, 'KaryakarGroup was successfully deleted.', 'alert-success'))


class HaribhaktDetailListView(ListView):
    model = HaribhaktDetail
    list_display = ('name','mobile_no')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class KaryakarGroupListView(ListView):
    model = KaryakarGroup
    list_display = ('group_id','karyakar','karyakar_from','karyakar_to','haribhakt')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['karyakargroups'] = KaryakarGroup.objects.filter(group_id='34')
        return context