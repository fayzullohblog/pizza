from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=60)
    email=serializers.EmailField(max_length=60)
    password=serializers.CharField(min_length=8)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)

    class Meta:
        model=User
        fields=['username','email','password','phone_number']

    def validate(self, attrs):
        
        
        username_exists=User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail='User username with exists')
        
        email_exists=User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User email with exists")

        password_exists=User.objects.filter(password=attrs['password']).exists()
       
        if password_exists:
            raise serializers.ValidationError(detail='User password with exists')
        print('phone------->',attrs['phone_number'])
        phonenumber_exists=User.objects.filter(phone_number=attrs['phone_number']).exists()
        print('-------12',phonenumber_exists)
        if phonenumber_exists:
            raise serializers.ValidationError(detail='User phone number with exists')

        return super().validate(attrs)
    



