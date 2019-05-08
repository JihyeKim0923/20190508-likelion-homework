from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from django.utils import timezone
from .forms import ScheduleForm

# Create your views here.

def home(request):
    schedules=Schedule.objects
    return render(request, 'myschedule/home.html',{'schedules':schedules})

def detail(request, schedule_id):
    schedule_detail= get_object_or_404(Schedule, pk= schedule_id)
    return render (request, 'myschedule/detail.html',{'schedule': schedule_detail})

def new(request):
    if request.method=="POST":
        form=ScheduleForm(request.POST)
        if form.is_valid():
            schedule=form.save(commit=False)
            schedule.published_date=timezone.datetime.now()
            schedule.save()
            return redirect('detail', schedule_id=schedule.pk)

    else:
        form=ScheduleForm()
    return render(request, 'myschedule/new.html',{'form':form})

def edit(request, schedule_id):
    schedule=get_object_or_404(Schedule, pk=schedule_id)
    if request.method=="POST":
        form=ScheduleForm(request.POST,instance=schedule)
        if form.is_valid():
            schedules=form.save(commit=False)
            schedules.published_date=timezone.datetime.now()
            schedules.save()
            return redirect('detail', schedule_id= schedule.pk)

    else:
        form=ScheduleForm(instance=schedule)
    return render(request, 'myschedule/edit.html',{'form':form})


def delete(request, schedule_id):
    schedules=get_object_or_404(Schedule, pk=schedule_id)
    schedules.delete()
    return redirect('home')