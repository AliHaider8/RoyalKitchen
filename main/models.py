from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime  

class Item(models.Model):
    LABELS = (
        ('BestSeller', 'BestSeller'),
        ('New', 'New'),
        ('Spicy🔥', 'Spicy🔥'),
    )   

    LABEL_COLOUR = (
        ('danger', 'danger'),
        ('success', 'success'),
        ('primary', 'primary'),
        ('info', 'info')
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    price = models.FloatField()
    pieces = models.IntegerField(default=6)
    instructions = models.CharField(max_length=250,default="Jain Option Available")
    image = models.ImageField(default='default.png', upload_to='images/')
    labels = models.CharField(max_length=25, choices=LABELS, blank=True)
    label_colour = models.CharField(max_length=15, choices=LABEL_COLOUR, blank=True)
    slug = models.SlugField(default="sushi_name")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:dishes", kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse("main:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_item_delete_url(self):
        return reverse("main:item-delete", kwargs={
            'slug': self.slug
        })

    def get_update_item_url(self):
        return reverse("main:item-update", kwargs={
            'slug': self.slug
        })

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    rslug = models.SlugField()
    review = models.TextField()
    posted_on = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review

class CartItems(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')
    delivery_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return self.item.title
    
    def get_remove_from_cart_url(self):
        return reverse("main:remove-from-cart", kwargs={
            'pk' : self.pk
        })

    def update_status_url(self):
        return reverse("main:update_status", kwargs={
            'pk' : self.pk
        })

class Login(models.Model):
   Username  = models.CharField(max_length=30,unique=True)
   password  = models.CharField(max_length=30,unique=True)
   Email     = models.CharField(max_length=50)
   EntryDate = models.DateTimeField()

class LoginDetail(models.Model):
	LoginID   = models.ForeignKey(Login, on_delete=models.CASCADE)
	Username  = models.CharField(max_length=30)
	Email     = models.CharField(max_length=50)
	LoginTime = models.DateTimeField()

class DistributerPersonalDetail(models.Model):
	FirstName     = models.CharField(max_length=30)
	LastName      = models.CharField(max_length=30)
	FatherName    = models.CharField(max_length=30)
	CNIC          = models.CharField(max_length=13,unique=True,blank=True)
	Age           = models.IntegerField()
	Gender        = models.CharField(max_length=8)
	MaritalStatus = models.CharField(max_length=10)
	EntryDate     = models.DateTimeField()

class DistributerContactDetail(models.Model):
   DistributerPID = models.ForeignKey(DistributerPersonalDetail,on_delete=models.CASCADE)
   Address        = models.CharField(max_length=100)
   City           = models.CharField(max_length=100)
   Country        = models.CharField(max_length=100)
   PhoneNo        = models.CharField(max_length=13)
   LandLineNo     = models.CharField(max_length=15,blank=True)
   Email          = models.CharField(max_length=50,blank=True)
   Others         = models.CharField(max_length=100,blank=True)
   EntryDate      = models.DateTimeField()

class DistributerBrandDetail(models.Model):
   DistributerPID = models.ForeignKey(DistributerPersonalDetail, on_delete=models.CASCADE)
   BrandName      = models.CharField(max_length=30,unique=True)
   Address        = models.CharField(max_length=100)
   Email          = models.CharField(max_length=50,unique=True,blank=True)
   PhoneNo        = models.CharField(max_length=13,unique=True)
   EntryDate      = models.DateTimeField()

class Ingredient(models.Model):
   IngredientName  = models.CharField(max_length=30,unique=True)
   IngredientPrice = models.DecimalField(max_digits=8, decimal_places=2)
   Size            = models.CharField(max_length=10,blank=True)
   Description     = models.CharField(max_length=100,blank=True)
   EntryDate       = models.DateTimeField()

class ProductPurchase(models.Model):
   BrandID       = models.ForeignKey(DistributerBrandDetail, on_delete=models.CASCADE)
   IngredientID  = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   PurchasePrice = models.DecimalField(max_digits=8, decimal_places=2)
   Quantity      = models.IntegerField() 
   Size          = models.CharField(max_length=10,blank=True)
   PurchaseDate  = models.DateTimeField()

class DistributerPayment(models.Model):
   DistributerPID = models.ForeignKey(DistributerPersonalDetail, on_delete=models.CASCADE)
   PurchaseID     = models.ForeignKey(ProductPurchase, on_delete=models.CASCADE)
   PaidAmount     = models.DecimalField(max_digits=8, decimal_places=2)
   RemaningAmount = models.DecimalField(max_digits=8, decimal_places=2) 
   PaymentMethod  = models.CharField(max_length=50)
   PaymentType    = models.CharField(max_length=13)
   EntryDate      = models.DateTimeField()

class CurrentStock(models.Model):
   IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   Quantity     = models.IntegerField()
   EntryDate    = models.DateTimeField()

class Food(models.Model):
   FoodName        = models.CharField(max_length=30,unique=True)
   FoodType        = models.CharField(max_length=50)
   FoodDescription = models.CharField(max_length=100,blank=True)
   EntryDate       = models.DateTimeField()

class FoodSize(models.Model):
   FoodID    = models.ForeignKey(Food, on_delete=models.CASCADE)
   FoodSize  = models.CharField(max_length=10)
   FoodPrice = models.DecimalField(max_digits=8, decimal_places=2) 
   EntryDate = models.DateTimeField()

class FoodIngredient(models.Model):
   FoodID       = models.ForeignKey(Food, on_delete=models.CASCADE)
   FoodSizeID   = models.ForeignKey(FoodSize, on_delete=models.CASCADE)
   IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   Quantity     = models.IntegerField()
   Size         = models.CharField(max_length=10)
   EntryDate    = models.DateTimeField()

class Offers(models.Model):
   OfferName    = models.CharField(max_length=30,unique=True)
   OfferPrice   = models.DecimalField(max_digits=8, decimal_places=2) 
   Availability = models.CharField(max_length=10,blank=True)
   CreateTime   = models.DateTimeField()

class OffersFood(models.Model):
   OfferID    = models.ForeignKey(Offers, on_delete=models.CASCADE)
   FoodID     = models.ForeignKey(Food, on_delete=models.CASCADE)
   FoodSizeID = models.ForeignKey(FoodSize, on_delete=models.CASCADE)
   Quantity   = models.IntegerField() 
   EntryDate  = models.DateTimeField()

class EmployeePesonalDetail(models.Model):
   FirstName     = models.CharField(max_length=30)
   LastName      = models.CharField(max_length=30,blank=True)
   CNIC          = models.CharField(max_length=13,unique=True,blank=True)
   FatherName    = models.CharField(max_length=30)
   Age           = models.IntegerField()
   Gender        = models.CharField(max_length=8)
   MaritalStatus = models.CharField(max_length=10)
   EntryDate     = models.DateTimeField()

class Employee(models.Model):
   EmployeePID       = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   JobName           = models.CharField(max_length=30)
   EmployeementYears = models.IntegerField()
   Salary            = models.DecimalField(max_digits=8, decimal_places=2) 
   Bonus             = models.DecimalField(max_digits=8, decimal_places=2) 
   DutyStartTime     = models.TimeField(blank=True)
   DutyEndTime       = models.TimeField(blank=True)
   JobDescription    = models.CharField(max_length=100)
   EntryDate         = models.DateTimeField()

class Customer(models.Model):
   FirstName = models.CharField(max_length=30)
   LastName  = models.CharField(max_length=30,blank=True)
   CNIC      = models.CharField(max_length=13,blank=True)
   PhoneNo1  = models.CharField(max_length=13,blank=True)
   Email     = models.CharField(max_length=50,blank=True)
   Address   = models.CharField(max_length=100,blank=True)
   EntryDate = models.DateTimeField(default=datetime.now(), blank=True)

class CustomerOrderBooking(models.Model):
   CustomerID  = models.ForeignKey(Customer, on_delete=models.CASCADE)
   EmployeePID = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE) 
   TotalBill   = models.DecimalField(max_digits=8, decimal_places=2) 
   EntryDate   = models.DateTimeField()

class CustomerOrderDetail(models.Model): 
   CustomerOrderID = models.ForeignKey(CustomerOrderBooking, on_delete=models.CASCADE) 
   ProductName     = models.CharField(max_length=30)
   ProductSize     = models.CharField(max_length=10)
   ProductQuantity = models.IntegerField()
   SalePrice       = models.DecimalField(max_digits=8, decimal_places=2) 
   EntryDate       = models.DateTimeField()

class EmployeeContactDetail(models.Model):
   EmployeePID = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   Address1    = models.CharField(max_length=100)
   City        = models.CharField(max_length=100) 
   Country     = models.CharField(max_length=100)
   PhoneNo1    = models.CharField(max_length=13,unique=True)
   LandLineNo  = models.CharField(max_length=15,blank=True)
   Email       = models.CharField(max_length=50,blank=True)
   EntryDate   = models.DateTimeField()

class Qualification(models.Model):
   EmployeePID   = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   DegreeName    = models.CharField(max_length=50)
   InstituteName = models.CharField(max_length=50)
   PassingYear   = models.CharField(max_length=10,blank=True)
   ObtainedMarks = models.IntegerField()
   TotalMarks    = models.IntegerField()
   Grade         = models.CharField(max_length=2,blank=True)
   Other         = models.CharField(max_length=100,blank=True)
   EntryDate     = models.DateTimeField()

class EmployeeSkill(models.Model):
   EmployeePID         = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   SkillName           = models.CharField(max_length=50)
   OrganizationName    = models.CharField(max_length=50)
   CertificationNumber = models.CharField(max_length=50,blank=True)
   LearnStartDate      = models.DateField()
   LearnEndDate        = models.DateField()
   Others              = models.CharField(max_length=100,blank=True)
   EntryDate           = models.DateTimeField()

class EmployeePrevoiusExperiance(models.Model):
   EmployeePID      = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   OrganizationName = models.CharField(max_length=50)
   JobName          = models.CharField(max_length=50)
   JobDescription    = models.CharField(max_length=100,blank=True)
   StartDate        = models.DateField()
   EndDate          = models.DateField()
   Others           = models.CharField(max_length=100,blank=True)
   EntryDate        = models.DateTimeField()

class CustomerOrderPayment(models.Model):
   CustomerOrderID  = models.ForeignKey(CustomerOrderBooking, on_delete=models.CASCADE) 
   PaymentMedium    = models.CharField(max_length=50)
   PaymentAmount    = models.DecimalField(max_digits=8,decimal_places=2)
   EntryDate        = models.DateTimeField()

class Delivery(models.Model):
   EmployeePID     = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   CustomerOrderID = models.ForeignKey(CustomerOrderBooking, on_delete=models.CASCADE) 
   DeliveryAddress = models.CharField(max_length=100)
   ExpectedTime    = models.CharField(max_length=10)
   EntryDate       = models.DateTimeField()

class Extras(models.Model):
   EmployeePID    = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   ExtrasName     = models.CharField(max_length=30)
   ExtrasType     = models.CharField(max_length=10)
   ExtrasQuantity = models.IntegerField(blank=True)
   Amount         = models.DecimalField(max_digits=8,decimal_places=2)
   Description    = models.CharField(max_length=250)
   EntryDate      = models.DateTimeField()


class product_insert(models.Model):
    product_name = models.CharField(max_length=100) 
    description = models.CharField(max_length=100) 
    Product_image = models.ImageField(upload_to='images/')

class reservation(models.Model):
   FirstName = models.CharField(max_length=30)
   LastName  = models.CharField(max_length=30,blank=True)
   Email     = models.CharField(max_length=50,blank=True)
   PhoneNo2  = models.CharField(max_length=13,blank=True)
   EntryDate = models.DateTimeField(default=datetime.now())
   numberofguests = models.CharField(max_length=13,blank=True)
   Timefrom = models.CharField(max_length=10)
   TimeTo = models.CharField(max_length=10)

# class picoffers(models.Model):
#     offers_name = models.CharField(max_length=100) 
#     describe = models.CharField(max_length=100) 
#     price = models.CharField(max_length=100) 
#     offers_image = models.ImageField(upload_to='images/')


class productimg(models.Model):
      image= models.ImageField(upload_to='images')
      name= models.CharField(max_length=100) 
      price= models.IntegerField(default=0)


