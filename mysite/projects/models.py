from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.box_size)


class ContentType(models.Model):

    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100, unique=True)

    def natural_key(self):
        return (self.title, self.subtitle)

    def __str__(self):
        return self.title


class Item(models.Model):

    title = models.CharField(max_length=100, unique=True, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to="images/", default="images/default.png")
    pub_date = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.title, self.pub_date)


class ItemImage(models.Model):
    image = models.ImageField(upload_to="images/", default="images/default.png")
    item = models.ForeignKey(Item, null=True, related_name='images')

    def __str__(self):
        return "%s, %s" % (self.image, self.item)
