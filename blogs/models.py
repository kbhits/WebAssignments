from django.db import models

# Create your models here.

class Topic(models.Model):
    #自我介绍的模块
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #返回模型的字符串表示
    def __str__(self):
        return self.text

class Entry(models.Model):
    #自我介绍的内容
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return self.text[:50] + "..."

class IntroduceTitle(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Introduce(models.Model):
    IntroduceTitle = models.ForeignKey(IntroduceTitle, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Introductions'
    def __str__(self):
        return self.text[:50] + "..."