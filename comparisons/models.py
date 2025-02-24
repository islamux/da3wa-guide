from django.db import models

class Religion(models.Model):
    name = models.CharField(max_length=100)  # اسم الدين
    principles = models.TextField()         # مبادئ الدين
    comparison_notes = models.TextField()   # ملاحظات المقارنة

    def __str__(self):
        return self.name