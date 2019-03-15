from django.db import models
from user.models import User
TYPES = (
    (1, "Associate"),
    (2, "Manager"),
    (3, "Handler"),
    (4, "Supervisor"),
)
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    emp_type = models.PositiveSmallIntegerField(choices=TYPES, default=1)

    def __str__(self):
        return self.user.username