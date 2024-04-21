from rest_framework import serializers
from base.models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class FAQCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    links = serializers.CharField(allow_blank=True)
    is_active = serializers.BooleanField()

    def validate_links(self, value: str) -> str:
        import re
        label_pattern = re.compile('^[a-zA-Z0-9-_.]+$')
        link_pattern = re.compile('^https?://([a-zA-Z0-9-_.:]+/?)*$')
        for idx, line in enumerate(value.splitlines()):
            if line.count(' ') != 1:
                raise serializers.ValidationError('Invalid links format')
            label, link = line.split(' ')
            if not label_pattern.match(label):
                raise serializers.ValidationError(f'Invalid link label format on line {idx + 1}')
            if not link_pattern.match(link):
                raise serializers.ValidationError(f'Invalid link link format on line {idx + 1}')

        return value

    def create(self, validated_data: dict) -> FAQ:
        return FAQ.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            links=self.links_json(validated_data['links']),
            is_active=validated_data['is_active']
        )

    def update(self, instance: FAQ, validated_data: dict) -> None:
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.links = self.links_json(validated_data['links'])
        instance.is_active = validated_data['is_active']
        instance.save()

    def links_json(self, links: str) -> str:
        from json import dumps
        res = dict()
        for line in links.splitlines():
            label, link = line.split(' ')
            res[label] = link
        return dumps(res)
