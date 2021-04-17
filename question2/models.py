from django.shortcuts import get_object_or_404
from django.db import models
from django.core.validators import MaxValueValidator

LIMIT = 2


class Slot(models.Model):
    slot = models.PositiveSmallIntegerField(primary_key=True, validators=[MaxValueValidator(23)]) 
    name = models.JSONField(default=list)

    @classmethod
    def book(cls, slot_number, new_person):
        """
        Method for booking a new slot, if possible
        :param slot_number: A number between 0 to 23
        :param new_person: Name of person who wants to book the slot
        :return: Object of Slot if the slot is booked or else None
        """

        slot, _ = cls.objects.get_or_create(slot=slot_number)
        persons = slot.name  # grabbing the persons who have previously booking the current slots

        if len(persons) < LIMIT:
            persons.append(new_person)
            slot.name = persons
            slot.save()

            return slot
        return None
        
    @classmethod
    def cancel(cls, slot_number, name):
        """
        Method for canceling a slot, if possible
        :param slot_number: A number between 1 to 23
        :param name: Name of the person who wants to cancel the booking
        :return: True if the slot could be canceled else False
        """

        slot = get_object_or_404(cls, slot=slot_number)

        if name in slot.name:
            slot.name.remove(name)

            # If other person has booked the same slot then save it else, delete the object
            if len(slot.name):
                slot.save()
            else:
                slot.delete()

            return True
        return False
