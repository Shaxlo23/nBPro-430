from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.urls import reverse
from django.utils.text import slugify
import uuid
# Create your models here.

class CustomUserManager(BaseUserManager): # BaseUserManager -> asosiy user boshqaruvi
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('Email ni bo\'sh qoldirish mumkinmas!')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)    
        extra_fields.setdefault('is_superuser',True)   

        return self.create_user(email,password,**extra_fields) 
    

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    phone_number=models.CharField(max_length=30,blank=False,null=False)
    avatar=models.ImageField(upload_to='images/',default='images/default.jpg',blank=True,null=False)
    slug=models.SlugField(blank=True, null=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=False)

    objects = CustomUserManager() #     `manager ulash


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(f"{self.first_name}-{self.last_name}-{str(uuid.uuid4())[:3]}")
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


#    USER PROFILE
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)


    def __str__(self):
        return f"{self.user.email} - Profile"
    

#SIGNAL: user yaratilganda avtomatik profile yaratadi

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

class Post(models.Model):

    #Foreignkey - bir user ko'p post yoza oladi
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(max_length=200)
    content = models.TextField()

    image = models.ImageField(
        upload_to='posts/',
        blank = True,
        null = True
    )

    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{str(uuid.uuid4())[:4]}')
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'slug':self.slug})
    
    def __str__(self):
        return f"{self.title}-{self.author.email}"