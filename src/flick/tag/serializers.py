from lst.simple_serializers import LstSimpleSerializer
from rest_framework import serializers
from show.simple_serializers import ShowSimpleSerializer

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    tag_id = serializers.CharField(source="id")
    shows = ShowSimpleSerializer(many=True, read_only=True)
    lsts = LstSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ("tag_id", "tag", "shows", "lsts")
        read_only_fields = fields
