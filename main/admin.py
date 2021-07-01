from django.contrib import admin
from .models import Item, CartItems, Reviews
from django.db import models
from .models import *

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Created By", {'fields': ["created_by"]}),
        ("Title", {'fields': ["title"]}),
        ("Image", {'fields': ["image"]}),
        ("Description", {'fields': ["description"]}),
        ("Price", {'fields': ["price"]}),
        ("Pieces", {'fields': ["pieces"]}),
        ("Instructions", {'fields': ["instructions"]}),
        ("Labels", {'fields': ["labels"]}),
        ("Label Colour", {'fields': ["label_colour"]}),
        ("Slug", {'fields': ["slug"]}),
    ]
    list_display = ('id','created_by','title','description','price','labels')

class CartItemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order Status", {'fields' : ["status"]}),
        ("Delivery Date", {'fields' : ["delivery_date"]})

    ]
    list_display = ('id','user','item','quantity','ordered','ordered_date','delivery_date','status')
    list_filter = ('ordered','ordered_date','status')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user','item','review','posted_on')

class classcustomer(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','CNIC','PhoneNo1','Email','Address','EntryDate']
class classlogin(admin.ModelAdmin):
    list_display=['id','Username','password','Email','EntryDate']
class classlogindetails(admin.ModelAdmin):
    list_display=['id','LoginID','Username','Email','LoginTime']
class classDistributerPersonalDetail(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','FatherName','CNIC','Age','Gender','MaritalStatus','EntryDate']
class classDistributerContactDetail(admin.ModelAdmin):
    list_display=['id','DistributerPID','Address','City','Country','PhoneNo','LandLineNo','Email','Others','EntryDate']
class classDistributerBrandDetail(admin.ModelAdmin):
    list_display=['id','DistributerPID','BrandName','Address','Email','PhoneNo','EntryDate']
class classDistributerBrandDetail(admin.ModelAdmin):
    list_display=['id','DistributerPID','BrandName','Address','Email','PhoneNo','EntryDate']
class classIngredient(admin.ModelAdmin):
    list_display=['id','IngredientName','IngredientPrice','Size','Description','EntryDate']
class classProductPurchase(admin.ModelAdmin):
    list_display=['id','BrandID','IngredientID','PurchasePrice','Quantity','Size','PurchaseDate']
class classDistributerPayment(admin.ModelAdmin):
    list_display=['id','DistributerPID','PurchaseID','PaidAmount','RemaningAmount','PaymentMethod','PaymentType','EntryDate']
class classCurrentStock(admin.ModelAdmin):
    list_display=['id','IngredientID','Quantity','EntryDate']
class classFood(admin.ModelAdmin):
    list_display=['id','FoodName','FoodType','FoodDescription','EntryDate']
class classFoodSize(admin.ModelAdmin):
    list_display=['id','FoodID','FoodSize','FoodPrice','EntryDate']
class classFoodIngredient(admin.ModelAdmin):
    list_display=['id','FoodID','FoodSizeID','IngredientID','Quantity','Size','EntryDate']
class classOffers(admin.ModelAdmin):
    list_display=['id','OfferName','OfferPrice','Availability','CreateTime']
class classOffersFood(admin.ModelAdmin):
    list_display=['id','OfferID','FoodID','FoodSizeID','Quantity','EntryDate']
class classEmployeePesonalDetail(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','CNIC','FatherName','Age','Gender','MaritalStatus','EntryDate']
class classEmployee(admin.ModelAdmin):
    list_display=['id','EmployeePID','JobName','EmployeementYears','Salary','Bonus','DutyStartTime','DutyEndTime','JobDescription','EntryDate']
class ClassCustomerOrderBooking(admin.ModelAdmin):
    list_display=['id','CustomerID','EmployeePID','TotalBill','EntryDate']
class ClassCustomerOrderDetail(admin.ModelAdmin):
    list_display=['id','CustomerOrderID','ProductName','ProductSize','ProductQuantity','SalePrice','EntryDate']
class ClassEmployeeContactDetail(admin.ModelAdmin):
    list_display=['id','EmployeePID','Address1','City','Country','PhoneNo1','LandLineNo','Email','EntryDate']
class ClassQualification(admin.ModelAdmin):
    list_display=['id','EmployeePID','DegreeName','InstituteName','PassingYear','ObtainedMarks','TotalMarks','Grade','Other','EntryDate']
class ClassEmployeeSkill(admin.ModelAdmin):
    list_display=['id','EmployeePID','SkillName','OrganizationName','CertificationNumber','LearnStartDate','LearnEndDate','Others','EntryDate']
class ClassEmployeePrevoiusExperiance(admin.ModelAdmin):
    list_display=['id','EmployeePID','OrganizationName','JobName','JobDescription','StartDate','EndDate','Others','EntryDate']
class ClassCustomerOrderPayment(admin.ModelAdmin):
    list_display=['id','CustomerOrderID','PaymentMedium','PaymentAmount','EntryDate']
class ClassDelivery(admin.ModelAdmin):
    list_display=['id','EmployeePID','CustomerOrderID','DeliveryAddress','ExpectedTime','EntryDate']
class ClassExtras(admin.ModelAdmin):
    list_display=['id','EmployeePID','ExtrasName','ExtrasType','ExtrasQuantity','Amount','Description','EntryDate']


admin.site.register(Item,ItemAdmin)
admin.site.register(CartItems,CartItemsAdmin)
admin.site.register(Reviews,ReviewsAdmin)
admin.site.register(Login,classlogin)
admin.site.register(LoginDetail,classlogindetails)
admin.site.register(DistributerPersonalDetail,classDistributerPersonalDetail)
admin.site.register(DistributerContactDetail,classDistributerContactDetail)
admin.site.register(DistributerBrandDetail,classDistributerBrandDetail)
admin.site.register(Ingredient,classIngredient)
admin.site.register(ProductPurchase,classProductPurchase)
admin.site.register(DistributerPayment,classDistributerPayment)
admin.site.register(CurrentStock,classCurrentStock)
admin.site.register(Food,classFood)
admin.site.register(FoodSize,classFoodSize)
admin.site.register(FoodIngredient,classFoodIngredient)
admin.site.register(Offers,classOffers)
admin.site.register(OffersFood,classOffersFood)
admin.site.register(EmployeePesonalDetail,classEmployeePesonalDetail)
admin.site.register(Employee,classEmployee)
admin.site.register(Customer,classcustomer)
admin.site.register(CustomerOrderBooking,ClassCustomerOrderBooking)
admin.site.register(CustomerOrderDetail,ClassCustomerOrderDetail)
admin.site.register(EmployeeContactDetail,ClassEmployeeContactDetail)
admin.site.register(Qualification,ClassQualification)
admin.site.register(EmployeeSkill,ClassEmployeeSkill)
admin.site.register(EmployeePrevoiusExperiance,ClassEmployeePrevoiusExperiance)
admin.site.register(CustomerOrderPayment,ClassCustomerOrderPayment)
admin.site.register(Delivery,ClassDelivery)
admin.site.register(Extras,ClassExtras)
admin.site.register(product_insert)
admin.site.register(reservation)
# admin.site.register(picoffers)
admin.site.register(productimg)
