from django.db import models

class BlogDetail(models.Model):
    tittle=models.CharField(max_length=255,  null=True, blank=False)
    image=models.ImageField(upload_to='blog/detail', null=True,blank=False)
    content=models.TextField()
    def __str__(self):
        return '{}'.format(self.tittle)
