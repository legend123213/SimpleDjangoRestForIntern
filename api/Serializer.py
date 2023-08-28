from rest_framework import serializers
from api.models import *
from Base.serializer import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserloginSerializer(serializers.ModelSerializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only = True)
        
        class Meta:
            model= User
            fields = ['username','password']
        def validate(self, data):
            user  = authenticate(username = data['username'] ,password = data.pop('password'))
            print(user)
            if user:
                refresh = RefreshToken.for_user(user)
                data['token_refresh'] = str(refresh)
                
                data['accuss'] = str(refresh.access_token)
                return data
            else:
                raise serializers.ValidationError('Invalid credentials')
        
            

class SkillSerializer(serializers.ModelSerializer):
    person_set = 'PersonSerializer'
    user_id = serializers.CharField(write_only= True)
    class Meta:
        model = Skill
        fields = ['id','language','Rate','user_id']
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username','email','password'] 
#     def create(self,validated_date):
#        user = User.objects.filter(validated_date.get('username'))
#        if user.exists():
#         #    raise ValidationError(message='User exists')

#             return user
#        else:
#             password = validated_date.pop('password')
#             registered_user = User.objects.create(username= validated_date['username'])
#             registered_user.set_password(password)
#             registered_user.save()
#             return registered_user
           
      
    # def create(self, validated_data):
        # user = self.request.context.get()
        # print(user)
        # return validated_data


    #     user =  PersonSerializer(Person.objects.get(Email = validated_data.pop('email')))
        # user = validated_data.pop("email")
        
        
        # if len(skillsToBeAdded)!= 0:
            # for i in validated_data:
            # skill =[Skill.objects.get_or_create(person = user,**skill_data)[0] for skill_data in skillsToBeAdded]
                # skill.append(Skill.objects.create(Person=user,language=i['language'],Rate=i['Rate']))
        #user = Person.objects.get(Email = validated_data.pop('email'))

        # skill = Skill.objects.create(person=user,**validated_data)
        # return skill
    # def update(self, instance, validated_data):
    #     instance.FullName = validated_data.get('FullName', instance.FullName)
    #     instance.BirthDate = validated_data.get('BirthDate', instance.BirthDate)
    #     instance.Email = validated_data.get('Email', instance.Email)
    #     instance.PhoneNumber = validated_data.get('PhoneNumber', instance.PhoneNumber)
    #     instance.SelfDescribtion = validated_data.get('SelfDescribtion', instance.SelfDescribtion)

    #     skills_data = validated_data.pop('Skills', [])
    #     skills_objs = [Skill.objects.get_or_create(**skill_data)[0] for skill_data in skills_data]
    #     instance.Skills.set(skills_objs)

    #     instance.save()
    #     return instance
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
# class UserSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)q
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']
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
    class Meta:
        model = Person
        depth = 1
        fields= ['FullName' ,'BirthDate','Email','PhoneNumber','SelfDescribtion','Street','City','Country','experience_set','project_set','skill_set','user_id']
    def create(self, validated_data):
        check =Person.objects.filter(Email = validated_data.get('Email'))
        if check.count>2:
            raise ValidationError(message="already exist you can only update",code=403)
        person = Person.objects.create(**validated_data)
        print(validated_data.get('user_id'))
        user = User.objects.get(id = validated_data.get('user_id'))
        person.user=user
        person.save()
        return person
    # def create(self, validated_data):
    #     email = validated_data.get('Email')
    #     user = 
    #     skills = validated_data.pop('Skills')
    #     user,_= Person.objects.get_or_create(**validated_data)
    #     for skill in skills:
    #         user.Skills.add(Skill.objects.create(**skill))

    #     return user
    




   