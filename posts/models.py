from django.db import models

# Create your models here.
class Post(models.Model): # has to extend django model
    text = models.TextField() # an attribute called text with type text field
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) # things happen to the post when author is deleted

    def __str__(self): # show customized instead of "Post object" in admin panel
        return self.text[:20]