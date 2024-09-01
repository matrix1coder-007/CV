from django.db import models

# Create your models here.
class Article(models.Model):
    article_s_num = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_record_created = models.DateTimeField(auto_now=True)
    article_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Blogs__article"

class Tag(models.Model):
    tag_s_num = models.AutoField(primary_key=True)
    article_s_num = models.ForeignKey("Article", on_delete=models.CASCADE)
    tag_title = models.CharField(max_length=30)
    tag_record_created = models.DateTimeField(auto_now=True)
    tag_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Blogs__tag"