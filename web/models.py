from django.db import models

# Create your models here.
class webdata1(models.Model):
    continent_n=models.CharField(max_length=50)
    # title_image=models.ImageField()
    desciption_1 = models.TextField()
    desciption_2 = models.TextField()
    desciption_3 = models.TextField()
    desciption_4 = models.TextField()
    description_5 = models.TextField(default="")
    description_6 = models.TextField(default="")
    title=models.CharField(max_length=100,default="")
    countries= models.JSONField(default=list)
    bg_image=models.ImageField(default="default_image.jpg")
    body_img1=models.ImageField(default="default_image.jpg")
    body_img2=models.ImageField(default="default_image.jpg")


class slugdata(models.Model):
    title1= models.CharField(max_length=100)
    bg_img=models.ImageField(default="default_image.jpg")

    body_img1=models.ImageField(default="default_image.jpg")
    heading_1=models.CharField(max_length=200)
    para_1 = models.TextField(default="")
    para_2 = models.TextField(default="")
    heading_2=models.CharField(max_length=100)
    body_img2=models.ImageField(default="default_image.jpg")
    para_3 = models.TextField(default="")
    heading_3=models.CharField(max_length=100,default="")
    para_4 = models.TextField(default="")
    body_img3=models.ImageField(default="default_image.jpg")
    heading_4=models.CharField(max_length=200,default="")
    para_5 = models.TextField(default="")
    para_6 = models.TextField(default="")
    para_7 = models.TextField(default="")
    body_img4=models.ImageField(default="default_image.jpg")
    heading_5=models.CharField(max_length=200)
    para_8 = models.TextField(default="")
    body_img5=models.ImageField(default="default_image.jpg")
    heading_6=models.CharField(max_length=200)
    para_9 = models.TextField(default="")
    body_img6=models.ImageField(default="default_image.jpg")
    heading_7=models.CharField(max_length=200)
    para_10 = models.TextField(default="")
    body_img7=models.ImageField(default="default_image.jpg")
    heading_8=models.CharField(max_length=200)
    para_11 = models.TextField(default="")
    heading_9=models.CharField(max_length=200)
    para_12 = models.TextField(default="")
    para_13 = models.TextField(default="")
    para_14 = models.TextField(default="")
    body_img8=models.ImageField(default="default_image.jpg")
    heading_10=models.CharField(max_length=200)
    para_15 = models.TextField(default="")
    heading_11=models.CharField(max_length=200)
    para_16 = models.TextField(default="")
    heading_12=models.CharField(max_length=200)
    heading_13=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,default="")
    heading_14=models.CharField(max_length=200,default="")
    heading_15=models.CharField(max_length=200,default="")
    heading_16=models.CharField(max_length=200,default="")
    para_17 = models.TextField(default="")
    







    


    

