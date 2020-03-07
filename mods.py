# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attributes(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=15)
    input_type = models.CharField(max_length=15)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attributes'


class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)
    brand_name = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brands'


#  done
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    parent_id = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    images = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryAttributes(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    attribute = models.ForeignKey(Attributes, models.DO_NOTHING)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category_attributes'


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    sender = models.ForeignKey('Users', models.DO_NOTHING)
    receiver = models.ForeignKey('Users', models.DO_NOTHING)
    message = models.TextField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chat'


class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    primary_image_id = models.IntegerField(blank=True, null=True)
    video = models.CharField(max_length=45, blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'images'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey('Users', models.DO_NOTHING)
    seller = models.ForeignKey('Users', models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'


# Done
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    slug = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seller_id = models.IntegerField()
    more_details = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING)
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    product_condition = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey('Users', models.DO_NOTHING)
    seller = models.ForeignKey('Users', models.DO_NOTHING)
    review_score = models.DecimalField(max_digits=10, decimal_places=0)
    average_score = models.DecimalField(max_digits=10, decimal_places=0)
    review = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'review'


class Roles(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_type = models.CharField(max_length=20)
    permission = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class SheImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    primary_image_id = models.IntegerField(blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    product_id = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'she_images'


class SheLocations(models.Model):
    locid = models.AutoField(db_column='LocId', primary_key=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'she_locations'


class SheProducts(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    slug = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seller_id = models.IntegerField()
    more_details = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING)
    brand_id = models.IntegerField(blank=True, null=True)
    product_condition = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    location = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'she_products'


class SheUsers(models.Model):
    matrikel_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateTimeField()
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=6)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    username = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    location = models.IntegerField()
    cat_preference = models.ForeignKey(Category, models.DO_NOTHING, db_column='cat_Preference')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'she_users'


class SheWishlist(models.Model):
    postid = models.IntegerField(db_column='PostId')  # Field name made lowercase.
    matrikel_number = models.CharField(db_column='Matrikel_number', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'she_wishlist'


class StudentArchives(models.Model):
    id = models.CharField(max_length=45)
    matrikel_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateTimeField()
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=6)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'student_archives'


class Users(models.Model):
    matrikel_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateTimeField()
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=6)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    username = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'

