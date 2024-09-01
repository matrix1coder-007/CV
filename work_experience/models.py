from django.db import models

# Create your models here.
class WorkExp(models.Model):

    WorkExp_Type = [
        ("Internship", "Intenships"),
        ("Full-Time", "Full-Time Professional"),
        ("Social Service", "Social Service")
    ]

    workexp_s_num = models.AutoField(primary_key=True)
    workexp_type = models.CharField(max_length=30, choices=WorkExp_Type)
    workexp_organization = models.CharField(max_length=500)
    workexp_location = models.TextField(max_length=100)
    workexp_industry = models.TextField(max_length=300)
    workexp_from = models.DateField()
    workexp_to = models.DateField(null=True)
    workexp_downloadable = models.BooleanField(default=False)
    workexp_record_created = models.DateTimeField(auto_now=True)
    workexp_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Work_Experience__work_exp"
