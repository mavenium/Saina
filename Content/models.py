from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from extensions.custom_validations import image_validation_by_size

from colorfield.fields import ColorField


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
    create_user = models.ForeignKey(
        User,
        verbose_name=_('Create User'),
        null=False,
        blank=False,
        editable=False,
        on_delete=models.PROTECT,
        related_name='sainalink_create_user'
    )
    last_update_user = models.ForeignKey(
        User,
        verbose_name=_('Last Update User'),
        null=False,
        blank=False,
        editable=False,
        on_delete=models.PROTECT,
        related_name='sainalink_last_update_user'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Saina Link")
        verbose_name_plural = _("Saina Links")

    def get_absolute_url(self):
        return f'/{self.slug}'


class SocialNetworksButton(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=128,
        null=False,
        blank=False
    )
    icon = models.CharField(
        verbose_name=_('Icon'),
        max_length=16,
        null=False,
        blank=False
    )
    url = models.URLField(
        verbose_name=_('URL'),
        null=False,
        blank=False
    )
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Social Networks Button")
        verbose_name_plural = _("Social Networks Buttons")


class Link(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=128,
        null=False,
        blank=False
    )
    url = models.URLField(
        verbose_name=_('URL'),
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")
