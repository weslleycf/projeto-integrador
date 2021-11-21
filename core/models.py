from django.contrib.auth.models import User
from django.db import models
from PIL import Image



class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Categoria')
    description = models.TextField(max_length=250, verbose_name='Descrição')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        verbose_name = 'Catergoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Serviço')
    categories = models.ManyToManyField(Category, verbose_name='Categoria', related_name='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    PHONE_TYPE = (
        ('RES', 'Residencial'),
        ('CEL', 'Celular'),
    )

    phone_number = models.CharField(max_length=11, verbose_name='Telefone', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phone_numbers')
    type = models.CharField(max_length=3, choices=PHONE_TYPE, verbose_name='Tipo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.phone_number


class Profile(models.Model):
    STATES = (('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
              ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
              ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
              ('PA', 'Pará'), ('PB','Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
              ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
              ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
              ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal'),
            )

    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário', related_name='profile')
    picture = models.ImageField(verbose_name='Foto', null=True, blank=True, default='profile_pics/default.png', upload_to='profile_pics')
    birth_date = models.DateField(verbose_name='Data de nascimento', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, verbose_name='Gênero', blank=True, null=True)
    services = models.ManyToManyField(Service, verbose_name='Serviço', blank=True, related_name='profiles')
    profile_description = models.TextField(max_length=500, verbose_name='Descrição', blank=True, null=True)
    social_number = models.CharField(max_length=11, verbose_name='CPF', unique=True, blank=True, null=True)
    zip_code = models.CharField(max_length=8, verbose_name='CEP', blank=True, null=True)
    street = models.CharField(max_length=100, verbose_name='logradouro', blank=True, null=True)
    number = models.CharField(max_length=8, verbose_name='Número', blank=True, null=True)
    complement = models.CharField(max_length=100, verbose_name='Complemento', blank=True, null=True)
    district = models.CharField(max_length=100, verbose_name='Bairro', blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='Cidade', blank=True, null=False)
    state = models.CharField(max_length=2, choices=STATES, verbose_name='Estado', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modificado em')




    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class Review(models.Model):
    RATING_VALUES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário', related_name='reviews')
    title = models.CharField(max_length=60, verbose_name='Título')
    comment = models.TextField(max_length=250, verbose_name='Comentário')
    rating = models.IntegerField(choices=RATING_VALUES, verbose_name='Nota')

    def __str__(self):
        self.title

