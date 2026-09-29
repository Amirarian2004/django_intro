from django.db import models

# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = [  # noqa: RUF012
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    # Or just this, So Ruff doesn't care.
    #     STATUS_CHOICES = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # ) 
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.CharField(max_length=300, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )
    is_featured = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title