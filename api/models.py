from django.db import models
from django.contrib.auth.models import AbstractUser


class Teachers(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile')

    def __str__(self) -> str:
        return f"{self.username}"

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="custom_user_set",  # Change related_name
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="custom_user_set",  # Change related_name
        help_text="Specific permissions for this user.",
    )


class Group(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} - {self.teacher.first_name}"
    
class Appartment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    appartment_user_firstname = models.CharField(max_length=30)
    appartment_user_lastname = models.CharField(max_length=30)
    info = models.TextField()
    image = models.ImageField(upload_to='appartment')

    def __str__ (self):
        return self.appartment_user_firstname + ' ' + self.appartment_user_lastname


class Stiuation(models.Model):
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)
    room_situation = models.IntegerField(default=0)
    heating_system = models.IntegerField(default=0)
    kitchen_system = models.IntegerField(default=0)
    description = models.TextField()
    imge_1 = models.ImageField(upload_to='stiuation', blank=True, null=True)
    imge_2 = models.ImageField(upload_to='stiuation', blank=True, null=True)
    imge_3 = models.ImageField(upload_to='stiuation', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.room_situation} - {self.appartment.appartment_user_firstname}"
    

class Students(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)
    CHOISE_TYPE = (
        ("ERKAK","ERKAK"),
        ("AYOL","AYOL"),
    )
    type = models.CharField(max_length=10, choices=CHOISE_TYPE)

    def __str__ (self):
        return self.firstname