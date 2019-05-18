from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """ Ticket model """

    def __str__(self):
        return self.subject

    subject = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    fk_status = models.ForeignKey(
        'Status',
        null=True,
        on_delete=models.SET_NULL,
        related_name='status_list',
    )
    fk_priority = models.ForeignKey(
        'Priority',
        null=True,
        on_delete=models.SET_NULL,
        related_name='priorities',
    )
    fk_requester = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    fk_agent = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
    )
    fk_attachments = models.ForeignKey(
        'Attachment',
        null=True,
        on_delete=models.SET_NULL,
        related_name='attachments',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )


class Status(models.Model):
    """ Status model """

    def __str__(self):
        return self.status

    status = models.CharField(
        null=False,
        max_length=255,
    )


class Priority(models.Model):
    """ Priority model """

    def __str__(self):
        return self.priority

    priority = models.CharField(
        null=False,
        max_length=255
    )


class Attachment(models.Model):
    """ Attachment model"""
    attachment = models.URLField(null=True)
