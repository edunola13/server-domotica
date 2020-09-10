# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver

from apps.manufacters.services.interfaces import ManufacterInterfaceService

from apps.devices.constants import RECEIVE_SYNC, RECEIVE_STATE

from apps.manufacters.models import Manufacter
from apps.devices.models import Device

from .events import send_signal, receive_signal


@receiver(receive_signal)
def receive(sender, **kwargs):
    services = ManufacterInternalService(
        manufacter=Manufacter.objects.get(kwargs['manufacter'])
    )
    services.receive(kwargs['device_id'], kwargs['data'])


class ManufacterInternalService(ManufacterInterfaceService):

    def __init__(self, manufacter):
        self.manufacter = manufacter

    def send(self, device, data):
        send_signal.send(
            sender=self.__class__,
            device_id=device.external_id,
            data=data
        )

    def receive(self, device_id, payload):
        device = Device.objects.get(external_id=device_id, manufacter=self.manufacter)
        if payload['type'] == RECEIVE_SYNC:
            device.receive_sync(payload)
        if payload['type'] == RECEIVE_STATE:
            device.receive_state(payload)
