from django.db import models

# Create your models here.

class Todo(models.Model):
    
    id=models.BigAutoField(
        primary_key=True
    )
    
    title=models.CharField(
        max_length=50,
        default=1,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Todo Title'
    )
    
    description=models.TextField(
        max_length=300,
        verbose_name='Description'
    )
    
    created_data=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Todo Create Date'
    )
    
    update_date=models.DateTimeField(
        auto_now=True,
    )
    
    status=models.BooleanField(
        default=False
    )
    
    rating=models.IntegerField(
        default=1
    )
    
    def _str_(self):
        return self.title
    
class department(models.Model):
        deptname=models.CharField(
            max_length=50,
            null=False,
            blank=False,
            unique=True,
        )
        description = models.TextField(
            max_length=300,
            verbose_name='Description'
        )
        def str(self):
            return self.deptname

class contact(models.Model):
        Name=models.CharField(
            max_length=50,
            null=False,
            blank=False,
            unique=True,
        )
        phonenumber=models.TextField(
            max_length=300,
            verbose_name='phonenumber'
        )


class Booking(models.Model):
      p_name = models.CharField(max_length=255)
      p_phone = models.CharField(max_length=10)
      p_email = models.EmailField()
      booking_date = models.DateField()
      booking_on = models.DateField(auto_now=True)  


      def _str_(self):
            return self.p_name
      
class Doctors(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_spec = models.TextField()
    dep_name = models.ForeignKey(department, on_delete = models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', default='default_image.jpg')

    def __str__(self):
        return 'DR' +' '+ self.doc_name +' - ('+ self.doc_spec + ')'