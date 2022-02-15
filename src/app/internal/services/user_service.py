from app.internal.models.tg_user import tgUser


def create_user(username: str) -> None:
    tgUser.objects.get_or_create(username=username)


def set_user_phone(username: str, phone: str) -> None:
    obj = tgUser.objects.get(username=username)
    obj.phone_number = phone
    obj.save()


def get_data(username: str) -> dict:
    user = tgUser.objects.filter(username=username)
    if user and user.first().phone_number:
        person = user.first()
        return {
            'phone_number': person.phone_number,
            'username': person.username
        }