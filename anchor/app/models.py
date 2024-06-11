from django.db import models


# Create your models here.
class user_registration(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    photo = models.FileField()
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Anchor_registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.IntegerField()
    gender= models.CharField(max_length=50)
    # account_number=models.CharField(max_length=50)
    profile=models.FileField()
    biodata = models.FileField()
    location = models.CharField(max_length=50)
    action=models.CharField(max_length=50)
    about_your_job=models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    # price=models.IntegerField()


    def __str__(self):
        return self.username

class PasswordReset(models.Model):
    user_registration = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    token = models.CharField(max_length=4)
class log_in(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    action=models.CharField(max_length=50)

    def __str__(self):
        return self.username



class ufeed(models.Model):
    username = models.CharField(max_length=55)
    anchorname = models.CharField(max_length=555)
    email= models.EmailField()
    feed = models.CharField(max_length=55)
    def __str__(self):
        return self.username

# class afeed(models.Model):
#     wname = models.CharField(max_length=55)
#     bname = models.CharField(max_length=555)
#     feed = models.CharField(max_length=55)
#     def __str__(self):
#         return self.wname
#forgot password
# class PasswordReset(models.Model):
#     user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
#     token = models.CharField(max_length=100, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.wname
class booking(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    PHONE =models.CharField(max_length=50)
    ADDRESS=models.CharField(max_length=50)
    EMAIL=models.CharField(max_length=50)
    DATE=models.DateField()
    ANCHOR=models.CharField(max_length=50)
    ACTION = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)
    # status = models.CharField(max_length=50)
    amount=models.IntegerField()

class payment(models.Model):
    username = models.CharField(max_length=50)
    PHONE =models.CharField(max_length=50)
    ADDRESS=models.CharField(max_length=50)
    EMAIL=models.CharField(max_length=50)
    DATE=models.DateField()
    ANCHOR=models.CharField(max_length=50)
    ACTION = models.CharField(max_length=50)
    payment =models.CharField(max_length=50)
    status=models.CharField(max_length=50)





class anchor_gallery(models.Model):
    username = models.CharField(max_length=50)
    photo = models.FileField()
    # photo1 = models.FileField()
    photo2 = models.FileField()
    photo3 = models.FileField()
    photo4 = models.FileField()
    photo5 = models.FileField()


class pay(models.Model):
    username = models.CharField(max_length=50)

class amountdetails(models.Model):
    username = models.CharField(max_length=50)
    fixedamount = models.IntegerField()
    advance = models.IntegerField()

