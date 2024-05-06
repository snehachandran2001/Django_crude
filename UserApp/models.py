from django.db import models


class DEPARTMENT(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.department_name


class EMPLOY(models.Model):
    employ_name = models.CharField(max_length=255)
    employ_mobile = models.CharField(max_length=255)
    employ_age = models.CharField(max_length=255)
    employ_department = models.ForeignKey(DEPARTMENT, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employ_table'

    def __str__(self):
        return self.employ_name