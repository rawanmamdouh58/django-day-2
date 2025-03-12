from django.shortcuts import render, redirect
from .models import Trainee  # Corrected import statement


def traineeList(request):
    trainees = Trainee.objects.all()
    return render(request, 'listtrainee.html', {"trainees": trainees})

def addTrainee(request):
    if request.method == 'POST':
        traineename = request.POST['name']
        traineeemail = request.POST['traineeEmail']
        traineeimgname = request.POST['traineeImg']

        Trainee.objects.create(name=traineename, email=traineeemail, image=traineeimgname)
        return redirect('traineeList')

    return render(request, 'addTrainee.html')

def updateTrainee(request, id):
    trainee = Trainee.objects.get(id=id)
    if request.method == 'POST':

        Trainee.objects.filter(id=id).update(
            name=request.POST['name'],
            email=request.POST['traineeEmail'],
            image=request.POST['traineeImg']
        )
        return redirect('traineeList')

    return render(request, 'editTrainee.html', {"trainee": trainee})

def deleteTrainee(request, id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('traineeList')