from django.db import models
from django.conf import settings


class VacancieManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(title__icontains=query) | \
            models.Q(name__icontains=query)
        )

class Vacancie(models.Model):
    
    name = models.CharField('Nome da Vaga', max_length=100)
    slug = models.SlugField('Atalho', max_length=100)
    salary = models.IntegerField('Faixa Salarial')
    educational = models.CharField('Escolaridade', max_length=100)
   
   
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = VacancieManager()

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return ('vacancies:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"
        ordering = ['name']

# class Enrollment(models.Model):

#     STATUS_CHOICES = (
#         (0, 'Pendente'),
#         (1, 'Aprovado'),
#         (2, 'Cancelado'),
#     )

#     user = models.ForeignKey(
#         #settings.AUTH_USER_MODEL, verbose_name='Usuário',
#         #related_name='enrollments'
#     )
#     #vacancie = models.ForeignKey(
#         #Vacancie, verbose_name='Vaga', related_name='enrollments'
#     )
#     status = models.IntegerField(
#         'Situação', choices=STATUS_CHOICES, default=1, blank=True
#     )

#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     updated_at = models.DateTimeField('Atualizado em', auto_now=True)

#     def active(self):
#         self.status = 1
#         self.save()

class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'Vacancie'),)