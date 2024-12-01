from django.core.exceptions import ValidationError


def validate_image(obj):
    filesize = obj.file.size
    megabyte_limit = 2
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError(f"Şəklin ölçüsü çox böyükdür. Maksiumum ölçü {megabyte_limit}MB ola bilər.")
