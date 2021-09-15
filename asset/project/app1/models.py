from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=255, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    publish_date = models.DateField(db_index=True)

    def __str__(self):
        return f"「{self.title}」{self.author}({self.publish_date})"

class Person(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    age = models.IntegerField(db_index=True)
    books = models.ManyToManyField(to=Book)

    def __str__(self):
        books_num = self.books.count()
        return f"{self.name} {self.age}歳 {books_num}冊"

class User(models.Model):
    first_name = models.CharField(max_length=255, db_index=True)
    last_name = models.CharField(max_length=255, db_index=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.age}歳"
