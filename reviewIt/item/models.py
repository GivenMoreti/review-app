from django.db import models

#review anything anonymously
class Item(models.Model):
    title = models.CharField(max_length=300,blank=True)  #what are your reviewing
    experience = models.TextField()                     #experience
    image_url = models.CharField(max_length=9000)
    relationship = models.CharField(max_length=300)     #association of the reviewer with item theyre reviewing
    location = models.CharField(max_length=300)
    stars = models.PositiveIntegerField(editable=True)
    date_time = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"You have reviewed {self.title}"
    
    class Meta:
        ordering = ["-date_time"]
