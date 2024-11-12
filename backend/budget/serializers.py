from rest_framework import serializers
from .models import Users
import re
from django.contrib.auth import authenticate

class UserSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['FirstName', 'LastName', 'Username', 'Password', 'Email', 'Birthday']

    def validate(self, data):
        errors = {}

        # Custom validation
        if len(data['FirstName']) < 5:
            errors['FirstName'] = "First Name must be at least 5 characters long."
        if len(data['LastName']) < 5:
            errors['LastName'] = "Last Name must be at least 5 characters long."
        if len(data['Username']) < 5:
            errors['Username'] = "Username must be at least 5 characters long."
        if len(data['Password']) < 8:
         errors['Password'] = "Password must be at least 8 characters long."
        if not re.search(r'\d', data["Password"]):
            errors['Password'] = "Password must contain at least one number"
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', data["Password"]):
            errors['Password'] = "Password must contain at least one special character"
        if errors:
            raise serializers.ValidationError(errors)
        
        return data

class LoginSeralizer(serializers.Serializer):
    Username = serializers.CharField()
    Password = serializers.CharField()

    def validate(self, data):
        username = data["Username"]
        password = data["Password"]

        user = authenticate(username = username, password = password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")
        
        return data

