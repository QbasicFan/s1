from django.db import models
# Create your models here.




class front(models.Model):
    text1 = models.CharField(max_length=200)
    text2 = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.text1


class section1(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class section2(models.Model):
    title = models.CharField(max_length=200)
    Text = models.CharField(max_length=500)

    productDate = models.DateTimeField(blank=True, null=True)
    productNumber = models.IntegerField(default=0)

    image = models.ImageField(upload_to='static/img/')


    def __str__(self):
        return self.title
