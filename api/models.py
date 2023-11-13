from django.db import models

# Create your models here.

class Post(models.Model):
    PROJECT_KIND = [
        ('study', 'study'),
        ('project', 'project'),
    ]

    STATUS_KIND = [
        ('online', 'online'),
        ('offline', 'offline'),
    ]

    DURATION_KIND = [
        ('1 개월', '1 개월'),
        ('2 개월', '2 개월'),
        ('3 개월', '3 개월'),
        ('4 개월', '4 개월'),
        ('5 개월', '5 개월'),
        ('6 개월', '6 개월'),
        ('1 년 이상', '1 년 이상'),
    ]


    recruit = models.ManyToManyField('accounts.User')
    position = models.ManyToManyField('api.Position')
    techstack = models.ManyToManyField('api.TechStack')

    kind = models.CharField(max_length=10, choices=PROJECT_KIND, default='study')
    status = models.CharField(max_length=10, choices=STATUS_KIND, default='online')
    duration = models.CharField(max_length=10, choices=DURATION_KIND, default='1 개월')
    deadline = models.DateField()
    kakao = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class TechStack(models.Model):
    icon = models.CharField(max_length=300)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name