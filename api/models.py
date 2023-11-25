from django.db import models

# Create your models here.

class Post(models.Model):
    PROJECT_KIND = [
        ('스터디', '스터디'),
        ('프로젝트', '프로젝트'),
    ]

    STATUS_KIND = [
        ('온라인', '온라인'),
        ('오프라인', '오프라인'),
    ]

    DURATION_KIND = [
        ('1개월', '1개월'),
        ('2개월', '2개월'),
        ('3개월', '3개월'),
        ('4개월', '4개월'),
        ('5개월', '5개월'),
        ('6개월', '6개월'),
        ('1년 이상', '1년 이상'),
    ]

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='posts_written')
    position = models.ManyToManyField('api.Position')
    techstack = models.ManyToManyField('api.TechStack')

    recruit = models.IntegerField(default=0)
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