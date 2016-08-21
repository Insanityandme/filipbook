from django.db import models


class CategoryManager(models.Manager):
    def get_by_natural_key(self, item_row_category):
        return self.get(item_row_category=item_row_category)


class ContentTypeManager(models.Manager):
    def get_by_natural_key(self, title, subtitle):
        return self.get(title=title, subtitle=subtitle)


# Create your models here.
class Category(models.Model):
    object = CategoryManager()

    name = models.CharField(max_length=100, unique=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class ContentType(models.Model):
    object = ContentTypeManager()

    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100, unique=True)

    def natural_key(self):
        return (self.title, self.subtitle)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True)
    subtitle = models.CharField(max_length=100, unique=True, blank=True)
    link = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="images/")
    pub_date = models.DateField(db_index=True, auto_now_add=True)

    category = models.ForeignKey(Category, null=True)
    content_type = models.ForeignKey(ContentType, null=True)

    def __str__(self):
        return "%s, %s" % (self.title, self.pub_date)


class ItemImage(models.Model):
    image = models.ImageField(upload_to="images/", default="SOME STRING")
    item = models.ForeignKey(Item, null=True, related_name='images')

    def __str__(self):
        return "%s, %s" % (self.image, self.item)
