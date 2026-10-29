from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


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
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,      # back to CASCADE
        null=True,
        blank=True,
        related_name='posts',
    )
    
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    