from django.db import models


class Item(models.Model):

    title = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(max_length=50, default="slug")
    content = models.TextField()
    excerpt = models.TextField(max_length=200)
    thumbnail = models.ImageField(upload_to="images/", default="images/default.png")
    hero = models.ImageField(upload_to="images/", default="images/hero.png")
    pub_date = models.DateField(db_index=True)

    def __str__(self):
        return "%s, %s" % (self.title, self.pub_date)


class ItemImage(models.Model):
    image = models.ImageField(upload_to="images/", default="images/default.png")
    item = models.ForeignKey(Item, null=True, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.image, self.item)
