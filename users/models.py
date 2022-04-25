from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from users.manager import CustomManager
# Create your models here.


class UserTable(AbstractUser):
    """customization of default User"""
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False, blank=False,
                                validators=[RegexValidator(r'[A-Za-z0-9@#$%^&+=]{6,}',
                                                           message='Must have atleast one: A-Z,a-z,0-9,sp. character')])
    first_name = models.CharField(max_length=150, validators=[RegexValidator(r'^[a-zA-Z .]+$',
                                                                            message='Must use ALPHA CHARACTERS only')])
    last_name = models.CharField(max_length=150, validators=[RegexValidator(r'^[a-zA-Z]+$',
                                                                           message='Must use ALPHA CHARACTERS only')])
    mobile_number = models.PositiveBigIntegerField(unique=True, blank=False, null=True)
    deactivate = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects_manager = CustomManager()

    def __str__(self):
        return str(self.first_name)