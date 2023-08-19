from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

def mya(request):
    return Response("Hello World")
class PersonalInfo(APIView):
    def post(self,request):
        return Response(data="Create user Person")
    def get(self ,request):
        return Response(data="get user information")
    def put(self,request):
        return Response("update user information")
class PersonExperiance(APIView):
    def post(self,request):
        return Response(data="Create user experiance")
    def get(self ,request):
        return Response(data="get user experiance")
    def delete(self,request):
        return Response("delete user experiance")        
class Experiance(APIView):
    def get(self ,request,id):
        return Response(data="get user experiance {id}".format(id=str(id)))
    def put(self,request,id):
        return Response({"it is deleted" + str(id)})
    def delete(self,request):
        return Response("delete user experiance")
class PersonProject(APIView):
    def post(self,request):
        return Response(data="Create user project")
        
    def get(self ,request):
        return Response(data="get user project")
    def delete(self,request):
        return Response("delete user project")  
class Projects(APIView):
    def get(self ,request,id):
        return Response(data="get user projects {id}".format(id=str(id)))
    def put(self,request,id):
        return Response({"it is deleted" + str(id)})
    def delete(self,request,id):
        return Response("delete user projects")
class PersonSkills(APIView):
    def post(self,request):
        return Response(data="Create user Skill")
    def get(self ,request):
        return Response(data="get user skills")
    def delete(self,request):
        return Response("delete user skills")  
    
class Skills(APIView):
    def get(self ,request,id):
        return Response(data="get user Skills {id}".format(id=str(id)))
    def put(self,request,id):
        return Response({"it is deleted" + str(id)})
    def delete(self,request):
        return Response("delete user Skills")
class Resume(APIView):
    def post(self,request):
        return Response(data="the link to download or the file to download")
    def get(self ,request,):
        return Response(data="get the link to view")
    def put(self,request,):
        return Response({"it is deleted" + str()})
    def delete(self,request):
        return Response("delete user Skills")