from django.db import models

# Create your models here.
class Contact(models.Model):

    Contact_Type = [
        ("Email", "Email"),
        ("LinkedIn", "LinkedIn"),
        ("Github", "Github"),
        ("GitLab", "GitLab"),
        ("Facebook", "Facebook")
    ]

    contact_s_num = models.AutoField(primary_key=True)
    contact_type = models.CharField(max_length=30, choices=Contact_Type)
    contact_link = models.TextField()
    contact_downloadable = models.BooleanField(default=False)
    contact_record_created = models.DateTimeField(auto_now=True)
    contact_record_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Contacts__contact"