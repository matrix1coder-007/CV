from django.db import models

# Create your models here.
class Merits(models.Model):

    Merit_Type = [
        ("Academic", "Academic"),
        ("Sports", "Sports"),
        ("Professional", "Professional") 
    ]

    merit_s_num = models.AutoField(primary_key=True)
    merit_type = models.CharField(max_length=30, choices=Merit_Type)
    merit_title = models.CharField(max_length=200)
    merit_year = models.DateField()
    merit_rank = models.IntegerField()
    merit_description = models.TextField()
    merit_organization = models.CharField(max_length=300)
    merit_downloadable = models.BooleanField(default=False)
    merit_record_created = models.DateTimeField(auto_now=True)
    merit_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Achievements__merits"