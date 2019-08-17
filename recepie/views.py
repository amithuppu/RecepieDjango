from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Step, Recipe, Ingredient
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class createRecepie(APIView):
    def post(self,request):
        try:
            data_type = request.content_type
            if data_type == "application/json":
                content = request.body.decode('utf-8')
                try:
                    data_json = json.loads(content)
                    user_count = User.objects.filter(username = data_json["username"]).count()
                    user_value = User.objects.filter(username=data_json["username"]).values()
                    recpie_name = data_json["name"]
                    if user_count == 0:
                        u1 = User(username= data_json["username"])
                        u1.save()
                        r1 = Recipe(name=recpie_name, user=u1)
                    else:
                        u1 = user_value[0]
                        r1 = Recipe(name=recpie_name, user_id=u1["id"])
                    r1.save()
                    ingredients_list = data_json["ingredients"]
                    steps_list  = data_json["steps"]
                    for each_ingredient in ingredients_list:
                        i1 = Ingredient(text= each_ingredient, recepie = r1)
                        i1.save()
                    for each_step in steps_list:
                        s1 = Step(step_text = each_step, recepie = r1)
                        s1.save()
                    return JsonResponse({'message': 'Recepie created successfully'})
                except Exception as e:
                    return JsonResponse({'message': 'Exception while creating the recepie'})
            else:
                return JsonResponse({'message': 'Expected JSON data. Other data found'})
        except Exception as e:
            return JsonResponse({'message': 'Exception while parsing'})



class getRecepiesByUser(APIView):
    def get(self,request):
        try:
            username = request.GET.get('username')
            u = User.objects.filter(username = username)
            recepies_list = []
            recepies = Recipe.objects.filter(user__in=u).values()
            count = Recipe.objects.filter(user__in=u).count()
            if count > 0:
                for i in range(0, count):
                    row = recepies[0]
                    recepies_list.append(row["name"])
            else:
                return JsonResponse({'message':'No recepies exist for user or user does not exist'})
            return JsonResponse({'recepies': recepies_list})
        except Exception as e:
            return JsonResponse({'message': 'Excpetion while getting the Recepies'})


class getallRecepies(APIView):
    def get(self,request):
        try:
            recepies_list = []
            recepies = Recipe.objects.all()
            count = Recipe.objects.all().count()
            for i in range(0, count):
                row = recepies[i]
                recepies_list.append(row.name)
            return JsonResponse({'recepies': recepies_list})
        except Exception as e:
            return JsonResponse({'message': 'Exception while getting all recepies'})


class deleteRecepie(APIView):
    def delete(self,request):
        try:
            recepiename = request.GET.get('recepie')
            Recipe.objects.filter(name=recepiename).delete()
            return JsonResponse({'message':'Recepie deleted successfully'})
        except Exception as e:
           return JsonResponse({'message': 'Error in recepie deletion process'})


class updateRecepie(APIView):
    def put(self,request):
        try:
            data_type = request.content_type
            if data_type == "application/json":
                content = request.body.decode('utf-8')
                try:
                    data_json = json.loads(content)
                    if "name" in data_json.keys():
                        recepie_name = data_json["name"]
                        r1 = Recipe.objects.filter(name=recepie_name).values()
                        print(r1)
                        print(r1[0])
                        if ("steps" not in data_json.keys()) and ("ingredients" not in data_json.keys()):
                            return JsonResponse({'message':'Either Steps or Ingredeints should be present. Nothing found'})
                        if "steps" in data_json.keys():
                            Step.objects.filter(recepie_id = r1[0]["id"]).delete()
                            steps_list = data_json["steps"]
                            for each_step in steps_list:
                                s1 = Step(step_text=each_step, recepie_id=r1[0]["id"])
                                s1.save()
                        if "ingredients" not in data_json.keys() :
                            Ingredient.objects.filter(recepie_id = r1[0]["id"]).delete()
                            ingredients_list = data_json["ingredients"]
                            for each_ingredient in ingredients_list:
                                i1 = Ingredient(text=each_ingredient, recepie_id=r1[0]["id"])
                                i1.save()
                        return JsonResponse({'message':' Recepie updated successfully'})
                    else:
                        return JsonResponse({'message':'recepie name not found in the data'})
                except Exception as e:
                    return JsonResponse({'message':'Exception while updating'})
            else:
                return JsonResponse({'message':'Expected JSON data. Other data found'})
        except Exception as e:
            return JsonResponse({'message': 'Exception while parsing the data'})


def index(request):
    return HttpResponse("Hello!")