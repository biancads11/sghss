from django.contrib.auth.hashers import make_password


def create_admin_user(apps):
    user = apps.get_model("core", "User")
    if not user.objects.filter(username="admin").exists():
        user.objects.create(
            username="admin",
            email="admin@example.com",
            name="Administrador",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            password=make_password("123456"),
        )