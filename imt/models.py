from django.db import models


# Create your models here.
class clearanceForm(models.Model):
   name = models.CharField(max_length=300, blank=False)
   reg_no = models.CharField(max_length=200, blank=False)
   email = models.EmailField(max_length=300, blank=False)
   phone = models.CharField(max_length=12, blank=False)
   department = models.CharField(max_length=200, blank=False)
   level = models.CharField(max_length=100, blank=False) 
   school = models.CharField(max_length=500, blank=True)
   
class registrationForm(models.Model):
   name = models.CharField(max_length=200, blank=False)
   app_no = models.CharField(max_length=300, blank=False)
   email = models.EmailField(max_length=300, blank=False)
   phone = models.CharField(max_length=12)
   department = models.CharField(max_length=300)
   level = models.CharField(max_length=30, blank=False)
   school = models.CharField(max_length=500, blank=True) 

class examForm(models.Model):
   name = models.CharField(max_length=200, blank=False)
   reg_no = models.CharField(max_length=200, blank=False)
   email = models.EmailField(max_length=200, blank=False)
   phone = models.CharField(max_length=12, blank=False)
   department = models.CharField(max_length=200, blank=False)
   description  = models.CharField(max_length=7000, blank=False) 
   school = models.CharField(max_length=500, blank=True)   

class regular_assessmentForm(models.Model):
   name =  models.CharField(max_length=300, blank=False)
   reg_no = models.CharField(max_length=50, blank=False)
   email =  models.CharField(max_length=200, blank=False)
   phone = models.CharField(max_length=12, blank=False)
   department = models.CharField(max_length=200, blank=False)
   description = models.CharField(max_length=5000, blank=False)
   school = models.CharField(max_length=500, blank=True)

class contactz_form(models.Model):
    name = models.CharField(max_length=200, blank=False )
    email = models.EmailField(max_length=200 ,blank=False)
    phone = models.CharField(max_length=12, blank=False)
    subject = models.CharField(max_length=300,blank=False)
    suggestion = models.CharField(max_length=5000, blank=False)
    message = models.CharField(max_length=2000, blank=False)

class projectForm(models.Model):
   name = models.CharField(max_length=200, blank=False)
   regno = models.CharField(max_length=300, blank=False)
   email = models.EmailField(max_length=300, blank=False)
   department = models.CharField(max_length=300, blank=False)
   phone = models.CharField(max_length=12, blank=False)
   message = models.CharField(max_length=2000, blank=False)
   project_topic = models.CharField(max_length=2000, blank=False)
   school = models.CharField(max_length=500, blank=True)    


class pd(models.Model):
   title = models.CharField(max_length=300, blank=True )
   body = models.TextField()

   def __str__(self):
      return self.title

#.................. for hot clearacnce Page .........................
class clearances_expalain(models.Model):
   title = models.CharField(max_length=100 , blank=True )
   body =  models.TextField()

   def __str__(self):
      return self.title   

#.................. for how to's Page .............................                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
class howtoz(models.Model):
   title = models.CharField(max_length=100,  blank=True )
   body = models.TextField(max_length=3000, blank=False)

   def __str__(self):
      return self.title 

