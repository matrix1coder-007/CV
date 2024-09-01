from django.db import models

# Create your models here.
class Visits(models.Model):
    visit_s_num = models.AutoField(primary_key=True)
    visit_destination = models.TextField()
    visit_year = models.DateTimeField()
    visit_description = models.TextField()
    visit_record_created = models.DateTimeField(auto_now=True)
    visit_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Footsteps__visits"

class VisitPics(models.Model):
    visit_pic_s_num = models.AutoField(primary_key=True)
    visit_s_num = models.ForeignKey("Visits", on_delete=models.CASCADE)
    visit_pic_img = models.ImageField(upload_to="static/images/footsteps")
    visit_pic_img_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Footsteps__visit_pics"