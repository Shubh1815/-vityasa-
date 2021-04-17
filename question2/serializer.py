from rest_framework import serializers
from .models import Slot


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

    def to_representation(self, obj):
        """
        If more then one person has booked a slot then display it as a array,
        else just display that single person.
        """

        data = {
            'slot': obj.slot,
            'name': obj.name
        }

        if len(data['name']) == 1:
            data['name'] = data['name'][0]

        return data
