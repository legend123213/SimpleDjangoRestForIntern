from rest_framework import serializers
from api.models import *
from Base.serializer import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate

        
            
class EducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    Person_id = serializers.CharField(write_only=True)
    class Meta:
        model = Education
        fields = ['id','NameOfSchool','CertifiedWith','Street','City','Country','DescribtionOfWork','DateFrom','DateTo','Person_id']

class LanguageSerialzer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    Person_id = serializers.CharField()
    class Meta:
        model = Language
        fields = ['id','Person_id','Language']
class SkillSerializer(serializers.ModelSerializer):
    person_set = 'PersonSerializer'
    
    user_id = serializers.CharField(write_only= True)
    class Meta:
        model = Skill
        fields = ['id','language','Rate','user_id']
        read_only =['id']
    def validate_Rate(self, value):
        if value > 10 :
            raise serializers.ValidationError("Please rate the skill between 0 to 10")
        return value   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password'] 
    def create(self,validated_date):
            password = validated_date.pop('password')
            registered_user = User.objects.create(username= validated_date['username'],email=validated_date['email'])
            registered_user.set_password(password)
            group = Group.objects.get(name= 'user_permission')
            group.user_set.add(registered_user)
            group.save()
            registered_user.save()
            return registered_user
           
      
 
class ExperienceSerializer(serializers.ModelSerializer):
    Email_id = serializers.CharField()
    class Meta:
        model = Experience
        fields = ['id','Email_id','NameOfCompany','Street','City','Country','Role','DescribtionOfWork','DateFrom','DateTo']

class ProjectSerializer(serializers.ModelSerializer):
    PersonId_id = serializers.CharField(write_only=True)
    class Meta:
        model = Project
        fields =['id','NameOfProject','Description','Link','PersonId_id']   
class PersonSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    project_set = ProjectSerializer(read_only = True,many = True)
    experience_set = ExperienceSerializer(read_only = True,many = True)
    skill_set = SkillSerializer(read_only = True,many =  True)
    language_set = LanguageSerialzer(read_only = True,many = True)
    education_set = EducationSerializer(read_only = True,many = True)
    class Meta:
        model = Person
        depth = 1
        fields= ['FullName' ,'BirthDate','UserRoll','PhoneNumber','Email','SelfDescribtion','Street','City','Country','experience_set','project_set','skill_set','user_id','language_set','education_set']
    def create(self, validated_data):
        check =Person.objects.filter(Email = validated_data.get('Email'))
        if check.count()>2:
            raise ValidationError(message="already exist you can only update",code=403)
        person = Person.objects.create(**validated_data)
        print(validated_data.get('user_id'))
        user = User.objects.get(id = validated_data.get('user_id'))
        person.user=user
        person.save()
        return person
 

