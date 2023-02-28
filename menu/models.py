from django.db import models
from django.urls import reverse


class MainMenu(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    main_menu = models.ForeignKey(MainMenu, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.title

