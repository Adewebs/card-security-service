from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Pupil(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    registration_number = models.CharField(max_length=200, unique=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    student_class = models.CharField(max_length=200, blank=True, null=True)
    skin_color = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    school_fee = models.CharField(max_length=200, null= True, blank=True)
    part_payment = models.CharField(max_length=200, blank=True, null=True)
    teachers_comment = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='userprofile/')
    QR_Code = models.ImageField(null=True, blank=True, upload_to="userQR/")
    Bar_Code = models.ImageField(null=True, blank=True, upload_to="userBar")
    parent = models.ForeignKey('ChildParents', related_name='pupils', on_delete=models.CASCADE)

class ChildParents(AbstractUser):
    title = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique = True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='parentsImage/')
    places_of_work = models.TextField(null=True, blank=True, max_length=50)
    address = models.TextField(null=True, blank=True)
    picker = models.CharField(max_length=20, null=True, blank=True)
    picker_description = models.TextField(blank=True, null=True)
    picker_number = models.CharField(max_length=20, null=True, blank=True)
    picker_security_question = models.CharField(max_length=100, null=True, blank=True)
    picker_security_answer = models.CharField(max_length=100, null=True, blank=True)
    parentqr = models.ImageField(null=True, blank=True, upload_to='parentsQR/')
    groups = models.ManyToManyField(Group, blank=True, related_name='parents')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='parents')
    # username = models.CharField(max_length=100,  blank=True, null=True,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"