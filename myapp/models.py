from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
def upload_to(instance, filename):
    """Generate upload path for user-uploaded files"""
    return f'blog_images/{instance.author.name}_{filename}'
    
class Post(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the post's title (max 200 characters).")
    content = models.TextField(help_text="Write the full content of the post.")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="Select the author who wrote this post.")
    cover_image = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        help_text="Upload a cover image for this post"
    )
    is_published = models.BooleanField(default=False, help_text="Mark as published to make the post visible to readers.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the post was created (auto-populated).")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
