from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from extensions.custom_validations import image_validation_by_size


class SainaLink(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=128,
        null=False,
        blank=False
    )
    description = models.CharField(
        verbose_name=_('Description'),
        max_length=265,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=32,
        null=False,
        blank=False,
        unique=True
    )
    logo = models.ImageField(
        verbose_name=_('Logo'),
        upload_to='logos',
        default='logos/default_logo.png',
        help_text=_('Max file size is %(size)d MB.') % {'size': settings.MAX_IMAGE_SIZE},
        validators=[image_validation_by_size],
        null=False,
        blank=True
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )
    last_update_time = models.DateTimeField(
        verbose_name=_('Last Update Time'),
        auto_now=True,
        null=False,
        blank=False,
        editable=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Saina Link")
        verbose_name = _("Saina Links")

    def get_absolute_url(self):
        return f'/{self.slug}'
