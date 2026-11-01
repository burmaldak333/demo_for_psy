from django.db import models


class Psychologist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание (Обо мне)")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    work_hours = models.CharField(max_length=100, verbose_name="Часы работы")
    social_link = models.URLField(verbose_name="Ссылка на соцсеть")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Психолог"
        verbose_name_plural = "Психологи"  # <--- Вот это меняет название


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    price = models.CharField(max_length=50, verbose_name="Цена (можно писать 'Бесплатно')")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"  # <--- И вот это


class Package(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название пакета")
    price = models.IntegerField(verbose_name="Цена (только цифры)")
    description = models.TextField(verbose_name="Описание пакета")
    features = models.TextField(verbose_name="Что входит (каждый пункт с новой строки)")
    is_popular = models.BooleanField(default=False, verbose_name="Сделать популярным?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пакет"
        verbose_name_plural = "Пакеты"  # <--- И вот это