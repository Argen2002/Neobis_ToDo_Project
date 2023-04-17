from django.db import models

# Create your models here.


# class TodoListItem(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name

#------------------------------------------------------------
class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=100)
    description = models.TextField('Описание',max_length=500)
    is_complete = models.BooleanField('Finish', default=False)
    created =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title