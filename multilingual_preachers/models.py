from django.db import models

class MultilingualPreacher(models.Model):
    name = models.CharField(max_length=100)         # اسم الداعية
    language = models.CharField(max_length=50)      # اللغة
    bio = models.TextField()                        # نبذة عن الداعية
    youtube_link = models.URLField(blank=True, null=True)  # رابط اليوتيوب
    facebook_link = models.URLField(blank=True, null=True) # رابط الفيسبوك

    def __str__(self):
        return f"{self.name} ({self.language})"