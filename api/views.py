from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from api.Permission import IsInGroup
from api.Serializer import *
from api.models import *
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
import json

class PersonalInfo(APIView):
    permission_classes = [IsAuthenticated,IsInGroup]

    def post(self, request):
        user = request.data
        user['Email'] = request.user.email
        user['user_id']= request.user.id
        user['person_id'] = User.objects.get(id = request.user.id)
        instance = PersonSerializer(data =  user)
        if instance.is_valid(raise_exception=True):
            instance.save()
            return Response(data=instance.data)
        else:
            return Response(data = "hello i do not think so")
        

    def get(self, request):
        print(request.user)
        users = User.objects.get(id = request.user.id)  
        user =get_object_or_404(Person,user_id=users.id)
        instance = PersonSerializer(user)
        print(instance)
        return Response(data=instance.data)
        

    def put(self, request):
        data = request.data
        user =get_object_or_404(Person,user_id=request.user.id)
        instance = PersonSerializer(data=data,instance=user)
        instance.is_valid(raise_exception=True)
        instance.save()

        return Response(data=instance.data)
    def delete(self,request):
        user_data = Person.objects.filter(user_id = request.user.email)
        delete = user_data.delete()
        print(delete)
        return Response(data={'message' :'all user personal Information deleted succussfully.'},status=status.HTTP_200_OK)

class PersonExperiance(APIView):
    permission_classes = [IsAuthenticated,IsInGroup]

    def post(self, request):
        data = request.data
        data['Email_id'] = request.user.email 
        instance = ExperienceSerializer(data=data)
        instance.is_valid(raise_exception=True)
        instance.save()
        
        return Response(data=instance.data,status=status.HTTP_201_CREATED)

    def get(self, request):
        
        user_experiance = Experience.objects.filter(Email_id = request.user.email)
        instance = ExperienceSerializer(user_experiance,many=True)
        return Response(data=instance.data)

    def delete(self, request):
        user_data = Experience.objects.filter(Email_id = request.user.email)
        delete = user_data.delete()
        print(delete)
        return Response(data={'message' :'all user skills deleted succussfully.'},status=status.HTTP_200_OK)



class Experiance(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def get(self, request, id):
        data = request.user
        user_experiance = Experience.objects.filter(Email_id = data.email)
        id_list =[int(id_num.id) for id_num in user_experiance]
        
        if id not in id_list:
            return Response(data = "there is no Experiance",status=status.HTTP_400_BAD_REQUEST)
        else:
            user_experiace = Experience.objects.get(id = id)
            instance = ExperienceSerializer(user_experiace)
            return Response(data=instance.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        return Response({"it is deleted" + str(id)})

    def delete(self, request,id):
        user_experiance = Experience.objects.filter(Email_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_experiance]
        if id not in id_list:
            return Response(data = "there is no Experiance",status=status.HTTP_400_BAD_REQUEST)
        user_experiace = Experience.objects.get(id = id)
        user_experiace.delete()
        return Response(data={'message' :'deleted succussfully.'},status=status.HTTP_200_OK)


class PersonProject(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
        data = request.data
        data['PersonId_id'] = request.user.email 
        instance = ProjectSerializer(data=data)
        instance.is_valid(raise_exception=True)
        instance.save()      
        return Response(data=instance.data,status=status.HTTP_201_CREATED)

    def get(self, request):
        Project_Instance =  Project.objects.filter(PersonId_id = request.user.email)
        Instance = ProjectSerializer(Project_Instance,many=True)
        return Response(data=Instance.data)


    def delete(self, request):
        user_data = Project.objects.filter(PersonId_id = request.user.email)
        delete = user_data.delete()
        print(delete)
        return Response(data={'message' :'all user Projects deleted succussfully.'},status=status.HTTP_200_OK)



class Projects(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def get(self, request, id):
        data = request.user
        user_projects = Project.objects.filter(PersonId_id = data.email)
        id_list =[int(id_num.id) for id_num in user_projects]
        if id not in id_list:
            return Response(data = "there is no Project",status=status.HTTP_400_BAD_REQUEST)
        else:
            user_skill = Project.objects.get(id = id)
            instance = ProjectSerializer(user_skill)
            return Response(data=instance.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        data = request.data
        data['PersonId_id'] = request.user.email
        del data['id']
        user_projects = Project.objects.filter(PersonId_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_projects]
        if id not in id_list:
            return Response(data = "there is no Project",status=status.HTTP_400_BAD_REQUEST)
        user_project = Project.objects.get(PersonId_id = request.user.email)
        instance = ProjectSerializer(data=data,instance=user_project)
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data=instance.data)

    def delete(self, request, id):
        user_projects = Project.objects.filter(PersonId_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_projects]
        if id not in id_list:
            return Response(data = "there is no Project",status=status.HTTP_404_NOT_FOUND)
        user_project = Person.objects.get(id = id)
        user_project.delete()
        return Response(data={'message' :'deleted succussfully.'},status=status.HTTP_200_OK)



class PersonSkills(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.email 
        instance = SkillSerializer(data=data)
        instance.is_valid(raise_exception=True)
        instance.save()      
        return Response(data=instance.data,status=status.HTTP_201_CREATED)


    def get(self, request):
        SkillInstance =  Skill.objects.filter(user_id = request.user.email)
        Instance = SkillSerializer(SkillInstance,many=True)
        return Response(data=Instance.data)

    def delete(self, request):
        user_data = Skill.objects.filter(user_id = request.user.email)
        delete = user_data.delete()
        print(delete)
        return Response(data={'message' :'all user skills deleted succussfully.'},status=status.HTTP_200_OK)


class Skills(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]
    
    def get(self, request, id):
        data = request.user
        user_skills = Skill.objects.filter(user_id = data.email)
        id_list =[int(id_num.id) for id_num in user_skills]
        if id not in id_list:
            return Response(data = "there is no Skill",status=status.HTTP_400_BAD_REQUEST)
        else:
            user_skill = Skill.objects.get(id = id)
            instance = SkillSerializer(user_skill)
            return Response(data=instance.data,status=status.HTTP_200_OK)


    def put(self, request, id):
        return Response({"it is deleted" + str(id)})

    def delete(self, request):
        user_skills = Skill.objects.filter(user_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_skills]
        if id not in id_list:
            return Response(data = "there is no skill",status=status.HTTP_404_NOT_FOUND)
        user_skill = Skill.objects.get(id = id)
        user_skill.delete()
        return Response(data={'message' :'deleted succussfully.'},status=status.HTTP_200_OK)



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
class Register(APIView):
    def post(self,request):
        data = request.data
        instance = UserSerializer(data=data)
        if instance.is_valid():
            user = instance.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginUser(APIView):
    def post(self,request):
        data =  request.data
        username = data['username']
        password = data['password']
        user = authentication
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return Response(data={"message":"login success"},status=status.HTTP_200_OK)
        else:
        
            
            return Response(data = {"message user not found"} ,status=status.HTTP_400_BAD_REQUEST)
    
    