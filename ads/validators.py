from rest_framework import serializers


def is_published_validator(value):
    if value:
        raise serializers.ValidationError('is_published cannot be True')
    return value
