from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    candidate_name = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    total_fees = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_joining = models.DateField(auto_now=False)

    def __str__(self):
        return f'{self.candidate_name} -- {self.course_name}'


class Invoice(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    enrollment_id = models.IntegerField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=False)
    reason = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.candidate
