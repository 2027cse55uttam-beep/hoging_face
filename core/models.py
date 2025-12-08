from django.db import models
from ckeditor.fields import RichTextField  # <--- 1. Import Zaroori Hai

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Project(models.Model):
    ICON_CHOICES = [
        ('fa-brands fa-python text-yellow-400', 'Python (Yellow)'),
        ('fa-brands fa-js text-yellow-300', 'JavaScript (Yellow)'),
        ('fa-brands fa-react text-blue-400', 'React (Blue)'),
        ('fa-solid fa-database text-indigo-400', 'Database/SQL (Indigo)'),
        ('fa-solid fa-server text-green-500', 'Django/Backend (Green)'),
        ('fa-solid fa-robot text-pink-500', 'AI/ML (Pink)'),
        ('fa-solid fa-cart-shopping text-orange-400', 'E-Commerce (Orange)'),
        ('fa-solid fa-layer-group text-purple-400', 'Full Stack (Purple)'),
    ]

    title = models.CharField(max_length=200)
    
    # 2. Galti Yahan Thi: 'models.RichTextField()' nahi, sirf 'RichTextField()' hoga
    description = RichTextField() 
    
    icon = models.CharField(max_length=100, choices=ICON_CHOICES, default='fa-solid fa-code')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title