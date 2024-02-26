from django.core.exceptions import ValidationError


def user_name_validator(username):
    for char in username:
        if not (char.isalnum() or char == '_'):
            raise ValidationError("Username must contain only letters, digits, and underscores!")


def custom_minlength_validator(username):
    if len(username) < 3:
        raise ValidationError("Username must be at least 3 chars long!")