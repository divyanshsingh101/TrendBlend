
from django.db import models
from unicodedata import decimal
from email.policy import default
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User


STATUS_CHOICE=(
   ("process" , "Processing"),
    ("shipped" , "Shipped"),
     ("delivered" , "Delivered"),

)

STATUS=(
   ("draft" , "Draft"),
   ("rejected" , "Rejected"),
   ("in_review" , "In Review"),
   ("published" , "Published"),

)
RATING=(
   (1 , "*"),
   (2 , "**"),
   (3 , "***"),
   (4 , "****"),
   (5 , "*****"),

)
def user_directory_path(instance,filename):
   return 'user_{0}/{1}'.format(instance.user.id,filename)
class Category(models.Model):
   cid=ShortUUIDField(unique=True, length=10,max_length=20 , prefix="cat", alphabet="abcdefgh12345") 
   title=models.CharField(max_length=100)
   image=models.ImageField(upload_to="category")
   class Meta :
      verbose_name_plural="categories"
   def category_image(self):
      
      return mark_safe('<img src="%s" width="50" />'%(self.image.url))
   def __str__(self):
      return self.title
#class Tags(models.Model):
   #pass
class Vendor(models.Model):
   vid=ShortUUIDField(unique=True, length=10,max_length=20 , prefix="ven", alphabet="abcdefgh12345") 
   
   title=models.CharField(max_length=100, default="nestify")
   image=models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
   description=models.TextField(null=True,blank=True, default="i am vendor")
   
   address=models.CharField(max_length=100, default="123 lucknow ")
   contact=models.CharField(max_length=100, default="+123 (456) 789 ")
   chat_resp_time=models.CharField(max_length=100, default="100 ")
   shipping_on_time=models.CharField(max_length=100, default="100")
   authentic_rating=models.CharField(max_length=100, default="100 ")
   days_return=models.CharField(max_length=100, default="100 ")
   warranty_period=models.CharField(max_length=100, default="100")

   user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
   class Meta:
      verbose_name_plural="vendors"
   def vendor_image(self):
      return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
   def __str__(self):
      return self.title
class Product(models.Model):
   pid=ShortUUIDField(unique=True, length=10, max_length=20, prefix="pr" , alphabet="abcdefgh12345")
   

   user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   Category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)

   title=models.CharField(max_length=100, default="fresh pear")
   image=models.ImageField(upload_to=user_directory_path, default="product.jpg")
   description=models.TextField(null=True,blank=True, default="this is product")
   
   price=models.DecimalField(max_digits=999999999, decimal_places=2, default="1299")
   old_price=models.DecimalField(max_digits=999999999, decimal_places=2, default="2299")

   specifications=models.TextField(null=True,blank=True)
   #tags=models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

   product_status=models.CharField(choices=STATUS,max_length=10, default="in_review")

   status=models.BooleanField(default=True)
   in_status=models.BooleanField(default=True)
   featured=models.BooleanField(default=False)
   digital=models.BooleanField(default=False)
    
   sku=ShortUUIDField(unique=True , length=4, max_length=10, prefix="sku" , alphabet="12334567890")

   date=models.DateTimeField(auto_now_add=True)
   updated=models.DateTimeField(null=True,blank=True)


   class Meta:
      verbose_name_plural="products"
   def vendor_image(self):
      return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
   def __str__(self):
      return self.title
   def get_percentage(self):
      new_price=(self.price / self.old_price)*100
      return new_price
class ProductImages(models.Model):
   images=models.ImageField(upload_to="product-images", default="product.jpg")
   product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
   date=models.DateTimeField(auto_now_add=True)

   class Meta:
      verbose_name_plural="products images"

######333333333333333333

class CartOrder(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   price=models.DecimalField(max_digits=999999999, decimal_places=2, default="1299")
   paid_track=models.BooleanField(default=False)
   order_date=models.DateTimeField(auto_now_add=True)
   product_status=models.CharField(choices=STATUS_CHOICE, max_length=30 , default="PROCESSING")

   class Meta:
       verbose_name_plural="Cart_order"

class CartOrderItems(models.Model):
   order=models.ForeignKey(CartOrder, on_delete=models.CASCADE)
   invoice_no=models.CharField(max_length=200)
   product_status=models.CharField(max_length=200)
   
   item=models.CharField(max_length=200)
   image=models.CharField(max_length=200)
   qty=models.IntegerField(default=0)
   price=models.DecimalField(max_digits=999999999, decimal_places=2, default="1299")
   total=models.DecimalField(max_digits=999999999, decimal_places=2, default="1299")
   
   class Meta:
      verbose_name_plural ="cart Order Items"

   def order_img(self):
      return mark_safe('img src="/media/%s" width="50" height="50 " />' %(self.image))
   
###############################################################################################################################################333333

class ProductReview(models.Model):
   user=models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
   product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
   review=models.TextField()
   rating=models.IntegerField(choices=RATING, default=None)
   date=models.DateTimeField(auto_now_add=True)
   class Meta:
      verbose_name_plural="product review"
   
   def __str__(self):
      return self.product.title
   def get_rating(self):
         return self.rating
   


class wishlist(models.Model):
   user=models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
   product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
 
   date=models.DateTimeField(auto_now_add=True)
   class Meta:
      verbose_name_plural="wishlists"
   
   def __str__(self):
      return self.product.title
  
class Address(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL , null=True)  
    address=models.CharField(max_length=100, null=True)
    status=models.BooleanField(default=False)

    class Meta:
      verbose_name_plural="address"
   
   



# Create your models here.

class Blog(models.Model):
  title=models.CharField(max_length=1000)
  created_at=models.DateTimeField(auto_now_add=True)
  description=models.CharField(max_length=550)

  def __str__(self):
    return self.title

