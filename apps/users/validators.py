from django.core.validators import RegexValidator

class NameValidator(RegexValidator):
    regex = r"^\w+$"
    message = (
        "enter name begins with capital letter and A-Z, a-z or _"
        " between 5 and 50 characters"
    )
    flags = 0

name_validator = NameValidator()