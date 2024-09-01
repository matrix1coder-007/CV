from django.db import models

# Create your models here.
class Project(models.Model):

    Project_Type = [
        ("Academic", "Academic"),
        ("Work", "Work"),
        ("Personal", "Personal"),
    ]

    Project_Nature = [
        ("Individual", "Individual"),
        ("Team", "Team"),
    ]

    project_s_num = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100)
    project_abstract = models.TextField()
    project_type = models.CharField(max_length=30, choices=Project_Type)
    project_organization = models.CharField(max_length=300)
    project_nature = models.CharField(max_length=30, choices=Project_Nature)
    project_from = models.DateField()
    project_to = models.DateField()
    project_downloadable = models.BooleanField(default=False)
    project_record_created = models.DateTimeField(auto_now=True)
    project_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Projects__project"