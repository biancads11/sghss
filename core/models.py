from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group
from django.db import models

# User's requested BaseModel, with 'updated_at' corrected to use auto_now=True.
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
        auto_now=True, # Corrected from auto_now_add=True
        editable=False
    )

    class Meta:
        abstract = True
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view')

# User's requested User model.
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
        through='UserGroup', # Explicit through model as requested
        blank=True,
        related_name='user_set',
        related_query_name="user",
    )

    # You must set USERNAME_FIELD to the field you want to use for login.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    class Meta:
        managed = True
        db_table = 'users'

# User's requested explicit through model for User-Group relationship.
class UserGroup(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE, # CASCADE is generally safer than DO_NOTHING
        db_column='id_user',
        related_name='user_group_relations', # Changed related_name to avoid clash
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE, # CASCADE is generally safer than DO_NOTHING
        db_column='id_group',
        related_name='user_relations', # Changed related_name to avoid clash
    )

    class Meta:
        managed = True
        db_table = 'user_groups'
        unique_together = ('user', 'group') # Ensures a user isn't in the same group twice

# --- Other Core Models ---

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

class AccessLog(BaseModel):
    """
    Corresponds to 'logs_acesso'
    Logs user access attempts.
    """
    user = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True, db_column='usuario_id')
    action = models.TextField()
    ip_address = models.GenericIPAddressField(db_column='ip_origem', null=True, blank=True)
    was_successful = models.BooleanField(db_column='sucesso')
    # Note: The 'data_hora' field is covered by 'created_at' from BaseModel.

    class Meta:
        db_table = 'logs_acesso'
        verbose_name = 'Access Log'
        verbose_name_plural = 'Access Logs'