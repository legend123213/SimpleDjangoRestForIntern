from django.db import models
from dateutil.relativedelta import relativedelta
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# validator
RateValidator = lambda input: None if input <= 10 else ValidationError("Please rate the skill between 0 to 10")


def RateValidator(rate):
    return None if rate <= 10 else ValidationError("Please rate the skill between 0 to 10")
# Create your models here.


class Skill(models.Model):
    language = models.CharField(max_length=15)
    Rate = models.IntegerField(validators=[RateValidator])
    user = models.ForeignKey('Person', on_delete=models.CASCADE, default='')

    @property
    def get_skillformat(self):
        return (self.language, self.Rate)

    class Meta:
        db_table = 'Skill'


class Person(models.Model):
    FullName = models.CharField(max_length=20)
    BirthDate = models.DateField(
        default=(datetime.datetime.now().date() - relativedelta(years=18)))
    Email = models.EmailField(primary_key=True, unique=True)
    PhoneNumber = models.CharField(max_length=30)
    UserRoll = models.CharField(max_length=40)
    SelfDescribtion = models.TextField()
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='person')

    class Meta:
        db_table = 'Person'


class Experience(models.Model):
    Email = models.ForeignKey(Person, on_delete=models.SET_DEFAULT, default='')
    NameOfCompany = models.CharField(max_length=30)
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Role = models.CharField(max_length=20)
    DescribtionOfWork = models.TextField()
    DateFrom = models.DateField(blank=True)
    DateTo = models.DateField(blank=True)

    class Meta:
        db_table = 'Experience'


class Project(models.Model):
    PersonId = models.ForeignKey(Person, on_delete=models.CASCADE)
    NameOfProject = models.CharField(max_length=50)
    Description = models.TextField()
    Link = models.URLField()

    class Meta:
        db_table = 'Project'
class Education(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.DO_NOTHING)
    NameOfSchool = models.CharField(max_length=30)
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    DescribtionOfWork = models.TextField() 
    CertifiedWith  = models.CharField(max_length=20)
    DateFrom = models.DateField(blank=True)
    DateTo = models.DateField(blank=True)
class Language(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    Language  = models.CharField(max_length=50)