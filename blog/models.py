from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('סכום הוצאה להשלמות. *הוספת תקציב תתבצע במינוס, לדוגמא -215', max_length=200)
    text = models.TextField('מידע נוסף')
    text1 = models.TextField('מידע נוסף 1')
    exp_super = models.CharField('סכום הוצאה לסופר. *הוספת תקציב תתבצע במינוס, לדוגמא -610', max_length=200)
    bal_super = models.CharField('יתרה סופר', max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title