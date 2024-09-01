from django.db import models

# Create your models here.
# education is an abstract parent model for inheritance by School and College classes
class Education(models.Model):
    edu_institute_s_num = models.AutoField(primary_key=True)
    edu_institute_name = models.TextField()
    edu_institute_address = models.CharField(max_length=500)
    edu_institute_from = models.DateField()
    edu_institute_to = models.DateField()
    edu_institute_board = models.CharField(max_length=500)
    edu_downloadable = models.BooleanField(default=False)
    edu_institute_website = models.CharField(max_length=1000, default="N/A")
    edu_institute_record_created = models.DateTimeField(auto_now=True)
    edu_institute_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# school has entries for playschool, mid-senior and higher secondary
class School(Education):
    school_pic = models.ImageField(upload_to="static/images/education/schools")

    class Meta:
        db_table = "Education__school"

# college has entries for bachelors and masters studies
class College(Education):
    college_pic = models.ImageField(upload_to="static/images/education/colleges")

    class Meta:
        db_table = "Education__college"