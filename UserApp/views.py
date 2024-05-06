from django.shortcuts import render, redirect
from . models import *
from django.db.models import Q


def input(request):
    data = DEPARTMENT.objects.all()

    if request.method == "POST":
        employ_name = request.POST.get('employ_name')
        employ_mobile = request.POST.get('employ_mobile')
        employ_age = request.POST.get('employ_age')
        employ_department = request.POST.get('employ_department')

        user_obj = EMPLOY()
        user_obj.employ_name = employ_name
        user_obj.employ_mobile = employ_mobile
        user_obj.employ_age = employ_age
        user_obj.employ_department = DEPARTMENT.objects.get(department_name=employ_department)

        user_obj.save()

        return redirect('table')

    return render(request, 'form.html', {'data_key': data})


def table(request):
    if request.method == "POST":
        search_any = request.POST.get('search_any')

        data = EMPLOY.objects.filter(Q(employ_name__icontains=search_any) |Q(employ_age__icontains=search_any) | Q(employ_mobile__icontains=search_any) | Q(employ_department__department_name__icontains=search_any))

        return render(request, 'table.html', {'data_key': data})
    data = EMPLOY.objects.all()
    return render(request, 'table.html', {'data_key': data})


def remove(request, id):
    col_remove = EMPLOY.objects.filter(id=id)

    col_remove.delete()

    return redirect('table')


def update(request, id):
    data = EMPLOY.objects.filter(id=id)
    data2 = DEPARTMENT.objects.all()

    if request.method == "POST":
        employ_name = request.POST.get('employ_name')
        employ_mobile = request.POST.get('employ_mobile')
        employ_age = request.POST.get('employ_age')
        employ_department = request.POST.get('employ_department')

        user_obj = EMPLOY.objects.get(id=id)

        user_obj.employ_name = employ_name
        user_obj.employ_mobile = employ_mobile
        user_obj.employ_age = employ_age
        user_obj.employ_department = DEPARTMENT.objects.get(department_name=employ_department)

        user_obj.save()

        return redirect('table')

    return render(request, 'update.html', {'data_key': data, 'data_key2': data2})