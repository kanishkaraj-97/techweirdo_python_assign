from os import EX_DATAERR
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

# Create your views here.
@csrf_exempt
def medicine(request):
    if(request.method == 'GET'):
        id = request.GET.get('id', '')
        name = request.GET.get('name', '')

        try:
            if(id!='' and name == ''):
                medicine_details = Medicine.objects.filter(id=id).all().values()
            elif(name!='' and id == ''):
                medicine_details = Medicine.objects.filter(name=name).all().values()
            else:
                return JsonResponse({'status':'failed', 'msg' : 'Enter either name or id. Atleast one in mandatory. You can enter only one.'}, status=300)

            if(medicine_details):
                return JsonResponse({'status':'sucess', 'data' : list(medicine_details)}, status=200)
            else:
                return JsonResponse({'status' : 'failed', 'msg' : 'No details found for {}'.format('id : '+id if id else 'name : '+name)}, status=400)
        except Exception as e:
                    return JsonResponse({'status' : 'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)

    elif(request.method == 'POST'):
        request_body = json.loads(request.body)

        if('name' in request_body and 'batch_no' in request_body and 'mnf_date' in request_body and 'expire_date' in request_body and 'type' in request_body):
            try:
                Medicine.objects.create(
                    name=request_body['name'],
                    batch_no=request_body['batch_no'],
                    mnf_date = request_body['mnf_date'],
                    expire_date = request_body['expire_date'],
                    type = request_body['type'],
                    quantity_measurment = request_body['quantity_measurment'] if 'quantity_measurment' in request_body else 'piece'
                )
            except Exception as e:
                return JsonResponse({'status':'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)
            
            return JsonResponse({'status' : 'sucess', 'msg' : 'Medicine details succesfully entered.'}, status=201) 
        else:
           return JsonResponse({'status':'failed', 'msg' : 'Required parametrs not sent.'}, status=400) 

@csrf_exempt
def users(request):
    if(request.method == 'GET'):
        id = request.GET.get('id', '')
        name = request.GET.get('first_name', '')

        try:
            if(id!='' and name == ''):
                user_details = Users.objects.filter(id=id).all().values()
            elif(name!='' and id == ''):
                user_details = Users.objects.filter(first_name=name).all().values()
            else:
                return JsonResponse({'status':'failed', 'msg' : 'Enter either first_name or id. Atleast one in mandatory. You can enter only one.'}, status=300)

            if(user_details):
                return JsonResponse({'status':'sucess', 'data' : list(user_details)}, status=200)
            else:
                return JsonResponse({'status' : 'failed', 'msg' : 'No details found for {}'.format('id : '+id if id else 'name : '+name)}, status=400)
        except Exception as e:
                    return JsonResponse({'status' : 'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)

    elif(request.method == 'POST'):
        request_body = json.loads(request.body)

        if('first_name' in request_body and 'last_name' in request_body and 'age' in request_body and 'address' in request_body and 'contact' in request_body):
            try:
                Users.objects.create(
                    first_name = request_body['first_name'],
                    last_name = request_body['last_name'],
                    age = request_body['age'],
                    address = request_body['address'],
                    contact = request_body['contact'],
                )
            except Exception as e:
                return JsonResponse({'status' : 'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)
            
            return JsonResponse({'status' : 'sucess', 'msg' : 'User details succesfully entered.'}, status=201) 
        else:
            return JsonResponse({'status':'failed', 'msg' : 'Required parametrs not sent.'}, status=400)

@csrf_exempt
def medicine_intake(request):

    if(request.method == 'GET'):
        user_id = request.GET.get('user', '')
        date = request.GET.get('date', '')
        status = request.GET.get('status', '')

        if(user_id and date and status):
            try:
                user = Users.objects.get(pk=int(user_id))
                if(user):
                    medicine_intake_list = MedicineIntakeSchedule.objects.filter(user=user, intake_date=date, status=status).all().values()

                    if(medicine_intake_list):
                        return JsonResponse({'status' : 'sucess', 'data' : list(medicine_intake_list)}, status=200)
                    else:
                        return JsonResponse({'status' : 'failed', 'msg' : 'No medicine found for current selection.'}, status=400)

                else:
                    return JsonResponse({'status' : 'failed', 'msg' : 'No medicine is assigned to user : {}'.format(user.first_name)}, status=400)
            except Exception as e:
                return JsonResponse({'status' : 'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)
        else:
            return JsonResponse({'status':'failed', 'msg' : 'Required parametrs not sent.'}, status=400)


    elif(request.method == 'POST'):
        request_body = json.loads(request.body)

        if('intake_time' in request_body and 'no_of_times_a_day' in request_body and 'intake_date' in request_body and 'medicine_id' in request_body and 'user_id' in request_body and 'quantity' in request_body):
            try:
                medicine = Medicine.objects.get(pk=request_body['medicine_id'])
                user = Users.objects.get(pk=request_body['user_id'])

                MedicineIntakeSchedule.objects.create(
                    intake_time = request_body['intake_time'],
                    no_of_times_a_day = request_body['no_of_times_a_day'],
                    intake_date = request_body['intake_date'],
                    medicine = medicine,
                    user = user,
                    quantity = request_body['quantity']
                )
            except Exception as e:
                return JsonResponse({'status' : 'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)
            
            return JsonResponse({'status' : 'sucess', 'msg' : 'Medicine Intake detail for User : {}  succesfully entered.'.format(user.first_name)}, status=201)
        else:
            return JsonResponse({'status':'failed', 'msg' : 'Required parametrs not sent.'}, status=400)
    
    elif(request.method == 'PATCH'):
        request_body = json.loads(request.body)

        if(len(request_body)):
            user_list = []
            for each in request_body:

                if('user' in each and 'medicine' in each and 'date' in each and 'intake_time' in each):
                    try:

                        user = Users.objects.get(pk=int(each['user']))
                        medicine = Medicine.objects.get(pk=int(each['medicine']))
                        medicine_intake_list = MedicineIntakeSchedule.objects.filter(user=user, medicine=medicine, intake_time=each['intake_time'], intake_date=each['date'])

                        if(medicine_intake_list):
                            user_list.append({user.first_name: medicine.name, "intake_time" : each['intake_time']})
                            medicine_intake_list.update(status='taken')

                    except Exception as e:
                        return JsonResponse({'status' : 'failed', 'msg' : 'An exception Occured. Details : {}'.format(e)}, status=500)
                else:
                    return JsonResponse({'status' : 'failed', 'msg' : 'Required parameters not sent.'}, status=400)

            return JsonResponse({'status' : 'sucess', 'msg' : 'All medicine intake for user list : {} sucessfully updated as taken.'.format(user_list)}, status=200)
        else:
            return JsonResponse({'status' : 'failed', 'msg' : 'Required parameters not sent.'}, status=400)


