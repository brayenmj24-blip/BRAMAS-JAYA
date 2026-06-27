from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_default_users(sender, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    admin_email = 'admin@gmail.com'
    admin_username = 'bramasadmin'
    admin_password = 'Admin@1234'
    if not User.objects.filter(username=admin_username).exists():
        user = User.objects.create_user(
            username=admin_username,
            email=admin_email,
            password=admin_password,
            first_name='Admin',
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

    customer_email = 'brayenmj24@gmail.com'
    customer_username = 'brayenmj24@gmail.com'
    customer_password = 'Customer@1234'
    if not User.objects.filter(username=customer_username).exists():
        user = User.objects.create_user(
            username=customer_username,
            email=customer_email,
            password=customer_password,
            first_name='Customer',
        )
        user.is_staff = False
        user.is_superuser = False
        user.save()


class TokoConfig(AppConfig):
    name = 'toko'

    def ready(self):
        post_migrate.connect(create_default_users, sender=self)
