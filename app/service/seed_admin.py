from app.modules.auth.model import User
import os

def create_admin_user():
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    admin = User.objects(email=admin_email).first()

    if admin:
        print("✔ Admin já existe")
        return

    admin = User(
        username="admin",
        email=admin_email,
        first_name="Admin",
        last_name="Admin",
        is_admin=True,
        is_active=True,
    )
    admin.set_password(admin_password)
    admin.save()

    print("🚀 Admin criado com sucesso")
