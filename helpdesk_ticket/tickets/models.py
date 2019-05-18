from django.db import models


class Ticket(models.Model):
    """ Ticket model """
    subject = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    fk_status = models.ForeignKey(
        'Status',
        on_delete=models.SET_NULL,
    )
    fk_priority = models.ForeignKey(
        'Priorities',
        on_delete=models.SET_NULL,
    )
    fk_requester = models.ForeignKey(
        'Users',
        on_delete=models.SET_NULL,
    )
    fk_agent = models.ForeignKey(
        'Users',
        on_delete=models.SET_NULL,
    )
    fk_attachments = models.ForeignKey(
        'Attachments',
        on_delete=models.SET_NULL,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )


class Status(models.Model):
    """ Status model """

    OPEN = 'OP'
    PENDING = 'PE'
    RESOLVED = 'RE'
    CLOSED = 'CL'
    STATUS_LIST = (
        (OPEN, 'Open'),
        (PENDING, 'Pending'),
        (RESOLVED, 'Resolved'),
        (CLOSED, 'Closed'),
    )

    status = models.CharField(
        null=False,
        max_length=2,
        choices=STATUS_LIST,
        default=OPEN,
    )


class Priorities(models.Model):
    """ Priorities model """

    LOW = 'LO'
    HIGH = 'HI'
    URGENT = 'UR'
    PRIORITIES_LIST = (
        (LOW, 'Low'),
        (HIGH, 'High'),
        (URGENT, 'Urgent'),
    )

    priority = models.CharField(
        null=False,
        max_length=2,
        choices=PRIORITIES_LIST,
        default=LOW,
    )


class Attachments(models.Model):
    """ Attachments model"""
    attachments = models.URLField(null=True)
