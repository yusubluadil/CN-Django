from django.db import models
from django.contrib.auth.models import User

from core.utils.image_size_validator import validate_image


"""
OneToOneField - Yəni bir user-in bir blogu ola bilər.
ForeignKey - Yəni bir user-in çoxlu blogu ola bilər.
ManyToManyField - Yəni çoxlu user-in çoxlu blogları ola bilər.
"""


"""
on_delete=models.SET_NULL (Yəni `User` obyekti silindiyi zaman ona aid olan `Blog` obyektlərinə `null` dəyər ver!)
QEYD: Əgər `on_delete=models.SET_NULL` verilərsə mütləq şəkildə `null=True` da verilməlidir!

on_delete=models.CASCADE (Yəni `User` obyekti silindiyi zaman ona aid olan `Blog` obyektləri də silinsin)
"""


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blogs')
    categories = models.ManyToManyField(Category)

    title = models.CharField(max_length=50)
    about = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', null=True, blank=True, validators=[validate_image])

    def __str__(self) -> str:
        try:
            return f'{self.author.username} <---> {self.title}'
        except:
            return f'null <---> {self.title}'

# user = User.objects.get(id=1)
# user.blogs.all()

# Blog.objects.filter(author=user)
# auto_now=True (Hər save metodu çağrıldığında yenilənir.)
# auto_now_add=True (İlk yaradılan zaman olan tarixi götürür.)
