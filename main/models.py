from django.db import models


class Info(models.Model):
    logo = models.ImageField()
    adress_title = models.CharField(max_length=255)
    adress_text = models.CharField(max_length=255)
    tel = models.IntegerField()
    time = models.DateTimeField()
    email = models.CharField(max_length=255)
    facebooke = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linked = models.CharField(max_length=255)

class logo(models.Model):
    logo1 = models.ImageField()
    logo2 = models.ImageField()
    logo3= models.ImageField()
    logo4 = models.ImageField()
    logo5 = models.ImageField()
    logo6 = models.ImageField()
    logo7 = models.ImageField()
    logo8 = models.ImageField()
    logo9 = models.ImageField()
    logo10 = models.ImageField()

class View(models.Model):
    title1 = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255)

    title2 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)

    title3 = models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)

    title4 = models.CharField(max_length=255)
    text4 = models.CharField(max_length=255)


class Project_text(models.Model):
    mini_text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

class Project(models.Model):
    img1 = models.ImageField()
    title1 = models.CharField(max_length=255)
    text1 = models.TextField()
    texts1 = models.CharField(max_length=255)




class About(models.Model):
    img = models.ImageField()
    img2 = models.ImageField()

    first_title1 = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)
    text1 = models.TextField()
    download = models.CharField(max_length=255)

    first_title2 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    text2 = models.TextField()


class Suppor(models.Model):
    

    img1 = models.ImageField()
    numers1 = models.IntegerField()
    title1 = models.CharField(max_length=255)

    

class Frequently_text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField() 
    title2 = models.CharField(max_length=255)

class Frequently(models.Model):
    question = models.CharField(max_length=255)
    ansver = models.CharField(max_length=255)

class Communyte(models.Model):
    
    imgs1 = models.ImageField()
   

    titles1 = models.CharField(max_length=255)
    texts1 = models.TextField()
    names1 = models.CharField(max_length=255)

   

class Conversion(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    data = models.DateTimeField()
    title = models.CharField(max_length=255)

