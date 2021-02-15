from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


def image_validation_by_size(image_file):
    image_file = image_file.file.size
    if image_file > settings.MAX_IMAGE_SIZE*1024*1024:
        raise ValidationError(_('Max file size is %(size)d MB.') % {'size': settings.MAX_IMAGE_SIZE})
