from django.db import models



class ContactUs(models.Model):
    full_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    msg_subject = models.CharField(max_length=30, null=True, blank=True)
    msg_content = models.TextField(max_length=240, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Email from {self.full_name} about {self.msg_subject}"