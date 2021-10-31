from django.db import models
from passlib.hash import pbkdf2_sha256
from django.utils import timezone

class User (models.Model):

    #user's username
    username = models.CharField(max_length=20, primary_key=True)

    #user's encrypted password
    password = models.CharField(max_length=20)

    #user's first emergency contact info
    EmergencyContactNameOne = models.CharField(max_length=20)
    EmergencyContactRelationOne = models.CharField(max_length=20)
    EmergencyContactPhoneOne = models.CharField(max_length=10)

    #user's second emergency contact info
    EmergencyContactNameTwo = models.CharField(default = '', max_length=20)
    EmergencyContactRelationTwo = models.CharField(default = '', max_length=20)
    EmergencyContactPhoneTwo = models.CharField(default = '', max_length=10)

    #user's third emergency contact info
    EmergencyContactNameThree = models.CharField(default = '', max_length=20)
    EmergencyContactRelationThree = models.CharField(default = '', max_length=20)
    EmergencyContactPhoneThree = models.CharField(default = '', max_length=10)

    # Compare raw password against encrypted password
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)

    def __str__(self):
        return self.username # field to be shown when called

class UserLogin (models.Model):

    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    password_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username # name to be shown when called

class TaskList (models.Model):

    description = models.CharField(max_length=20) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # date field
    task_creator = models.ForeignKey(User, on_delete=models.CASCADE) # foreign key that links created tasks to a user (many-to-one)

    class Meta:
        ordering = ["-created"] # order tasks by date created 

    def __str__(self):
        return self.description # field to be shown when called
    
    

    

    