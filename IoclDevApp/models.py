# Create your models here.
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


# class Tag(models.Model):
#         EmergencyContectperson_name =  models.CharField(max_length=250,null=True)
#         # EmergencyContectperson_ph_no = models.CharField(max_length=50,null=True)
#         def __str__(self):
#             return f"{self.name}"


class Customer(models.Model):
    name = models.CharField(max_length=50,null=True)
    pic =  models.ImageField(default="Adherdoc.png", null=True, blank=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=("Enter a valid international mobile phone number starting with +(country code)"))
    ph_no =  models.CharField(validators=[phone_regex], verbose_name=("Mobile phone"), max_length=17, blank=True, null=True)
    alternative_ph_no = models.CharField(validators=[phone_regex], verbose_name=("Mobile phone"), max_length=17, blank=True, null=True)
    Email = models.CharField(max_length=50,null=True)
    Created_date = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200,null=True)
    nearestpolicestation = models.CharField(max_length=200,null=True)
    #tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name}: {self.ph_no}: {self.Email}:{self.Created_date}"


class Device_Info(models.Model):
    CATAGARY = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Sold', 'Sold'),
			)
    device_no = models.CharField(max_length=50,null=True)
    customer = models.ForeignKey(Customer, null =True, on_delete = models.SET_NULL)
    device_type =  models.CharField(max_length=50,null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    device_location = models.CharField(max_length=200,null=True)
    m2m_reg_no = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=200, null=True, choices=CATAGARY)
    Active_status = models.BooleanField(default=1)


    def __str__(self):
        return f"{self.device_no}: {self.device_type}: {self.date_created}:{self.Active_status}"

class MainFeed(models.Model):
    # Customername = models.CharField(max_length=200,null=True)
    Customer = models.ForeignKey(Customer, null =True, on_delete = models.SET_NULL)
    Device_Info = models.ForeignKey(Device_Info, null =True, on_delete = models.SET_NULL)
    address = models.CharField(max_length=200,null=True)
    ph_no = models.CharField(max_length=50,null=True)
    weight = models.FloatField(null=True)
    gasVal = models.CharField(max_length=50,null=True)
    paymentStatus = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.Customer}: {self.ph_no}: {self.weight}:{self.gasVal}:{self.paymentStatus}"

class PaymentStatus(models.Model):
    Customer = models.ForeignKey(Customer, null =True, on_delete = models.SET_NULL)
    Device_Info = models.ForeignKey(Device_Info, null =True, on_delete = models.SET_NULL)
    last_payment_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=0)
    remarks = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.Customer}: {self.Device_Info}: {self.last_payment_date}:{self.status}"
    
# class PremiumCustomer(models.Model):
#     Customer = models.ForeignKey(Customer, null =True, on_delete = models.SET_NULL)
#     Device_Info = models.ForeignKey(Device_Info, null =True, on_delete = models.SET_NULL)
#     validate = models.DateTimeField(auto_now_add=True, null=True)
#     phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=("Enter a valid international mobile phone number starting with +(country code)"))
#     ph_no =  models.CharField(validators=[phone_regex], verbose_name=("Mobile phone"), max_length=17, blank=True, null=True)
#     alternative_ph_no = models.CharField(validators=[phone_regex], verbose_name=("Mobile phone"), max_length=17, blank=True, null=True)
#     Email = models.CharField(max_length=50,null=True)
#     Created_date = models.DateTimeField(auto_now_add=True, null=True)
#     address = models.CharField(max_length=200,null=True)
#     nearestpolicestation = models.CharField(max_length=200,null=True)
    #tags = models.ManyToManyField(Tag)

class Transiction(models.Model):
    CustomerName = models.CharField(max_length=50,null=True)
    QR_Data = models.CharField(max_length=150,null=True)
    Qr_no = models.CharField(max_length=50,null=True)
    uid = models.CharField(max_length=50,null=True)
    Purches_date = models.DateTimeField(auto_now_add=True, null=True)
    OTP = models.CharField(max_length=50,null=True,blank=True)
    Ph_No = models.CharField(max_length=50,null=True,blank=True)
    Sale_date = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    DisplayFields = ['CustomerName','QR_Data', 'Qr_no', 'Purches_date','OTP', 'Ph_No', 'Sale_date','status']
    SerchFilds = ['OTP','Ph_No']
    FilterFilds = ['CustomerName','status']
    class Meta:
        db_table = "Transiction"

    # def __str__(self):
    #     return f"{self.CustomerName}: {self.QR_Data}: {self.Qr_no}:{self.Purches_date}"

class Qrdatatable(models.Model):
    CustomerName = models.CharField(max_length=50,null=True)
    QR_Data = models.CharField(max_length=150,null=True)
    Qr_no = models.CharField(max_length=50,null=True)
    uid = models.CharField(max_length=50,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    Imgpath = models.CharField(max_length=200,null=True)
    DisplayFields = ['CustomerName','QR_Data', 'Qr_no', 'uid','created_date','Imgpath']
    SerchFilds = ['Qr_no','Ph_No']
    FilterFilds = ['CustomerName']
    class Meta:
        db_table = "Qrdatatable"
        