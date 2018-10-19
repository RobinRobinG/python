from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[A-Za-z\d+-._]+@[A-Za-z\d+-._]+.[A-Za-z]+$')

class UserManager(models.Manager):
    def loginValidation(self, postData):
        errors = []
        try:
            user = User.objects.get(email=postData['email'])
            pw = postData['password'].encode()
            if bcrypt.hashpw(pw, user.password.encode()) == user.password.encode():
                return user
            else:
                errors.append('Invalid password')
                return errors
        except:
            errors.append('Username does not exist')
            return errors

    def registerValidation(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append('First name should be at least 2 letters.')
        if not postData['first_name'].isalpha():
            errors.append('First name should contain only letters.')
        if len(postData['last_name']) < 2:
            errors.append('Last name should be at least 2 letters.')
        if not postData['last_name'].isalpha():
            errors.append('Last name should contain only letters.')

        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid email')
        else:
            try:
                e = User.objects.get(email=postData['email'])
                errors.append('Email is associated with an existing user')
            except:
                pass
        try:
            y, m, d = map(int, postData['birthdate'].split('-'))
            birthdate = datetime(y, m, d)
            if birthdate > datetime.now():
                errors.append('Birthdate must be before today!')
        except:
            errors.append('Birthdate field required')

        if postData['password'] != postData['confirm']:
            errors.append('Passwords do not match')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters long')

        if len(errors) == 0:
            hashedpw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashedpw, birthdate=birthdate)
            return user
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"