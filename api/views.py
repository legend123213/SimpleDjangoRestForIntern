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
       
        users = User.objects.get(id = request.user.id)  
        user =get_object_or_404(Person,user_id=users.id)
        instance = PersonSerializer(user)
        
        return Response(data=instance.data)
        

    def put(self, request):
        data = request.data
        data['user_id'] = request.user.id
        data['Email']= request.user.email
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
        data['Email'] = Person.objects.get(user_id=request.user.id)
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
        data = request.data
        data['Email_id'] = request.user.email
        if 'id' in data : del data['id']
        user_experiances = Experience.objects.filter(Email_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_experiances]
        if id not in id_list:
            return Response(data = "there is no Project",status=status.HTTP_400_BAD_REQUEST)
        user_project = Experience.objects.get(Email_id = request.user.email)
        instance = ExperienceSerializer(data=data,instance=user_project)
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data=instance.data)

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
        if 'id' in data : del data["id"]
        user_projects = Project.objects.filter(PersonId_id = request.user.email)
        
        id_list =[int(id_num.id) for id_num in user_projects]
        if id not in id_list:
            return Response(data = "there is no Project",status=status.HTTP_400_BAD_REQUEST)
        user_project = user_projects.get(id =id)
        instance = ProjectSerializer(data=data,instance=user_project)
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data=instance.data)

    def delete(self, request, id):
        user_projects = Project.objects.filter(PersonId_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_projects]
        if id not in id_list:
            return Response(data = "there is no Project",status=status.HTTP_404_NOT_FOUND)
        user_project = user_projects.get(id=id)
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
        if SkillInstance.count ==0:
            return Response(data={"user skill":SkillInstance},status=status.HTTP_404_NOT_FOUND)
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
            user_skill = user_skills.get(id = id)
            instance = SkillSerializer(user_skill)
            return Response(data=instance.data,status=status.HTTP_200_OK)


    def put(self, request, id):
        data = request.data
        data['user_id']= request.user.email
        if 'id' in data : del data['id']
        user_skills = Skill.objects.filter(user_id = request.user.email)
       
        id_list =[int(id_num.id) for id_num in user_skills]
        if id not in id_list:
            return Response(data = "there is no Skill",status=status.HTTP_400_BAD_REQUEST)
        user_skill = user_skills.get(id = id )
        instance = SkillSerializer(instance=user_skill,data = data)
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data =instance.data,status=status.HTTP_200_OK )

    def delete(self, request,id):
        user_skills = Skill.objects.filter(user_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_skills]
        if id not in id_list:
            return Response(data = "there is no skill",status=status.HTTP_404_NOT_FOUND)
        user_skill = user_skills.get(id = id)
        user_skill.delete()
        return Response(data={'message' :'deleted succussfully.'},status=status.HTTP_200_OK)



class Resume(APIView):
    permission_classes = [IsAuthenticated, IsInGroup]

    def post(self, request):
        return Response(data="the link to download or the file to download")

    def get(self, request):
        users = User.objects.get(id = request.user.id)  
        user =get_object_or_404(Person,user_id=users.id)
        instance = PersonSerializer(user).data
        name = instance['FullName'].split()
       
        instance['F_name'] = name[0]
        instance['L_name'] = name[1]
        print(instance['UserRoll'])
        return render(request,'index1.html',instance)

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
            print(refresh)
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
class Educations(APIView):
    def get(self,request):
        user = Education.objects.filter(Person_id = request.user.email)
        if user.count ==0:
            return Response(data={"user education":user},status=status.HTTP_404_NOT_FOUND)
        instance = EducationSerializer(user,many=True)
        return Response(data=instance.data,status=status.HTTP_200_OK)
    def post(self,request):
        userdata = request.data
        userdata['Person_id'] = request.user.email
        if id in userdata : del userdata['id']
        instance = EducationSerializer(data=userdata)
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data=instance.data,status=status.HTTP_201_CREATED)
    def delete(self,request):
        user = Education.objects.get(Person_id = request.user.email)
        if user.count ==0:
            return Response(data={"data":user},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(data={"message":"deleted succeful"},status=status.HTTP_200_OK)
class Educationpersonal(APIView):
    def get(self,request,id):
        userdata = Education.objects.filter(Person_id = request.user.email)
       
        list_of_education = [user.id for user in userdata]
        if id in list_of_education:
            instance = EducationSerializer(userdata.get(id=id))
            return Response(data=instance.data ,status=status.HTTP_200_OK)
        
        return Response(data = {"message":"there no education list"},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,id):
        education = request.data
        userdata = Education.objects.filter(Person_id = request.user.email)
       
        list_of_education = [user.id for user in userdata]
        if id in list_of_education:
            instance = EducationSerializer(instance= userdata.get(id=id),data=education)
            instance.is_valid(raise_exception=True)
            instance.save()
            return Response(data=instance.data ,status=status.HTTP_200_OK)
        return Response(data={"message":"you can not edit"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        userdata = Education.objects.filter(Person_id = request.user.email)
       
        list_of_education = [user.id for user in userdata]
        if id in list_of_education:
            delete_data = userdata.get(id= id)
            instance = EducationSerializer(delete_data.delete())

            return Response(data=instance.data ,status=status.HTTP_200_OK)
        return Response(data={"message":"you can not edit"},status=status.HTTP_400_BAD_REQUEST)
        
class Personal_languages(APIView):
    def get(self,request):
        data = Language.objects.filter(Person_id = request.user.email)
        if data.count ==0:
            return Response(data={"user":data},status=status.HTTP_404_NOT_FOUND)
        instance = LanguageSerialzer(data,many =True)
        return Response(data=instance.data,status=status.HTTP_200_OK)
    def post(self,request):
        user_data = request.data
        user_data['Person_id'] = request.user.email
        instance = LanguageSerialzer(data=user_data)
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data=instance.data,status=status.HTTP_201_CREATED) 
    def delete(self,request):
        data = Language.objects.filter(Person_id = request.user.email)
        user_deleted_data = data.delete()
        instance = LanguageSerialzer(user_deleted_data)
        return Response(data=instance.data,status=status.HTTP_200_OK)
class Person_language(APIView):
    def get(self,request,id):
        user_language = Language.objects.filter(Person_id = request.user.email)
        user_id_list = [user.id for user in user_language]
        if id not in user_id_list:
            return Response(data={"message":"you can not edit"},status=status.HTTP_400_BAD_REQUEST)
        instance = LanguageSerialzer(user_language.get(id=id))

        return Response(data=instance.data,status=status.HTTP_200_OK)
    def put(self,request,id):
        user_data = request.data
        if 'id' in user_data: del user_data['id']
        user_data['Person_id'] = request.user.email
        user_language = Language.objects.filter(Person_id = request.user.email)
        user_id_list = [user.id for user in user_language]
        if id not in user_id_list:
            return Response(data={"message":"you can not edit"},status=status.HTTP_400_BAD_REQUEST)
        instance = LanguageSerialzer(data=user_data,instance=user_language.get(id = id))
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(data=instance.data,status=status.HTTP_200_OK)
    def delete(self,request,id):
        user_languages = Language.objects.filter(Person_id = request.user.email)
        id_list =[int(id_num.id) for id_num in user_languages]
        if id not in id_list:
            return Response(data = "there is no language",status=status.HTTP_404_NOT_FOUND)
        user_language = user_languages.get(id = id)
        user_language.delete()
        return Response(data={'message' :'deleted succussfully.'},status=status.HTTP_200_OK)

