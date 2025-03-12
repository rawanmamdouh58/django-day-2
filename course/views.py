from django.shortcuts import render, redirect
from .models import Course  # Corrected import statement


def courseList(request):
    courses = Course.objects.all()
    return render(request, 'courseList.html', {"courses": courses})


def addCourse(request):
    if request.method == 'POST':
        coursename = request.POST['name']
        courseimgname = request.POST['courseImg']
        Course.objects.create(name=coursename, image=courseimgname)
        return redirect('courseList')

    return render(request, 'courseForm.html')


def updateCourse(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        Course.objects.filter(id=id).update(
            name=request.POST['name'],
            image=request.POST['courseImg']
        )
        return redirect('courseList')

    return render(request, 'editCourse.html', {"course": course})



def deleteCourse(request, id):
    Course.objects.filter(id=id).update(status=False)
    return redirect('courseList')