from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from simple_history.models import HistoricalRecords


@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    if not User.objects.filter(username="admin").exists():
        User.objects.create(
            name="Administrador",
            username="admin",
            email="admin@example.com",
            password=make_password("123456"),
            is_superuser=True,
            is_staff=True,
        )


class BaseModel(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        db_column='updated_at',
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view')


class User(AbstractUser, PermissionsMixin, BaseModel):
    name = models.CharField(
        db_column='name',
        max_length=255,
        null=False,
    )
    username = models.CharField(
        db_column='username',
        max_length=255,
        unique=True,
        null=False,
    )
    email = models.EmailField(
        db_column='email',
        max_length=255,
        unique=True,
        null=False,
    )
    password = models.CharField(
        db_column='password',
        max_length=255,
        null=False,
    )
    groups = models.ManyToManyField(
        Group,
        through='UserGroup',
        blank=True,
        related_name='user_set',
        related_query_name="user",
    )
    history = HistoricalRecords(table_name='"history"."usuarios"')

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = make_password("123456")
        else:
            if not self.password.startswith("pbkdf2_"):
                self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'usuarios'


class UserGroup(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        db_column='id_user',
        related_name='user_group_relations',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        db_column='id_group',
        related_name='user_relations',
    )

    class Meta:
        managed = True
        db_table = 'user_groups'
        unique_together = ('user', 'group')


class AccessProfile(BaseModel):
    """
    Corresponds to 'perfis_acesso'
    Defines roles and their permissions within the system.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    permissions_json = models.JSONField(db_column='permissoes_json', blank=True, null=True)

    class Meta:
        db_table = 'perfis_acesso'
        verbose_name = 'Access Profile'
        verbose_name_plural = 'Access Profiles'


class AuthenticationToken(BaseModel):
    """
    Corresponds to 'tokens_autenticacao'
    Stores authentication tokens for users.
    """
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, db_column='usuario_id')
    token_hash = models.TextField()
    expiration = models.DateTimeField(db_column='expiracao')
    is_active = models.BooleanField(db_column='ativo', default=True)

    class Meta:
        db_table = 'tokens_autenticacao'
        verbose_name = 'Authentication Token'
        verbose_name_plural = 'Authentication Tokens'
