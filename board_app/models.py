from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


tanks = "TA"
healers = "HE"
dd = "DD"
merchants = "ME"
guild_masters = "GM"
quest_givers = "QG"
blacksmiths = "BL"
tanners = "TA"
potion_makers = "PM"
spell_masters = "SM"

CATEGORIES = (
        (tanks, "Танки"),
        (healers, "Хилы"),
        (dd, "ДД"),
        (merchants, "Торговцы"),
        (guild_masters, "Гилдмастеры"),
        (quest_givers, "Квестгиверы"),
        (blacksmiths, "Кузнецы"),
        (tanners, "Кожевники"),
        (potion_makers, "Зельевары"),
        (spell_masters, "Мастера заклинаний")
    )


class Advertisement(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255, unique=True)
    text_ad = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORIES, default=quest_givers)
    upload = models.ImageField(blank=True, null=True, upload_to='content')

    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('advertisement_detail', args=[str(self.id)])


class Response(models.Model):
    text_of_response = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)