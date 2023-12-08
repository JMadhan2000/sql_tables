from django.db import models

# Create your models here.

class dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)

    def __str__(self):
        return self.dname 

class emp(models.Model):
    emp_number=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    deptno=models.OneToOneField(dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name


class bonus(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()

    def __str__(self):
        return self.job
      

class salgrade(models.Model):
    grade=models.CharField(max_length=100)
    place_of_work=models.CharField(max_length=100)
    emp_no=models.OneToOneField(bonus,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.grade

    