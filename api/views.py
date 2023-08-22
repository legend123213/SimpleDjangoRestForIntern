from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from api.Permission import IsInGroup
from api.Serializer import *
from api.models import *
import json

class PersonalInfo(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
       
        print(type(UserSerializer(request.user).data))
        print(request.user.email)
        user = request.data
        userrr =  UserSerializer(request.user).data
        
        # user['user']=userrr
        instance = PersonSerializer(data =  user)
        if instance.is_valid(raise_exception=True):
            instance.save()
            return Response(data=instance.data)
        else:
            return Response(data = "hello i do not think so")
        

    def get(self, request):
        
        users = User.objects.get(id = request.user.id)
        
        user = get_object_or_404(Person)
        
        instance = PersonSerializer(user)
        return Response(data=instance.data)
        

    def put(self, request):
        return Response("update user information")


class PersonExperiance(APIView):
    permission_classes = [IsAuthenticated,IsInGroup]

    def post(self, request):
        return Response(data="Create user experiance")

    def get(self, request):
        return Response(data="get user experiance")

    def delete(self, request):
        return Response("delete user experiance")


class Experiance(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def get(self, request, id):
        return Response(data="get user experiance {id}".format(id=str(id)))

    def put(self, request, id):
        return Response({"it is deleted" + str(id)})

    def delete(self, request):
        return Response("delete user experiance")


class PersonProject(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
        return Response(data="Create user project")

    def get(self, request):
        return Response(data="get user project")

    def delete(self, request):
        return Response("delete user project")


class Projects(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def get(self, request, id):
        return Response(data="get user projects {id}".format(id=str(id)))

    def put(self, request, id):
        return Response({"it is deleted" + str(id)})

    def delete(self, request, id):
        return Response("delete user projects")


class PersonSkills(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
        return Response(data="Create user Skill")

    def get(self, request):
        skills = Skill.objects.all()
        print(skills)
        instance = SkillSerializer(skills)
        print(instance)
        return Response(data=instance.data)

    def delete(self, request):
        return Response("delete user skills")


class Skills(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def get(self, request, id):
        return Response(data="get user Skills {id}".format(id=str(id)))

    def put(self, request, id):
        return Response({"it is deleted" + str(id)})

    def delete(self, request):
        return Response("delete user Skills")


class Resume(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
        return Response(data="the link to download or the file to download")

    def get(self, request,):
        return Response(data="get the link to view")

    def put(self, request,):
        return Response({"it is deleted" + str()})

    def delete(self, request):
        return Response("delete user Skills")
