from rest_framework import serializers
from base.models import Project, User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CreateProjectSerializer(serializers.Serializer):
    name = serializers.CharField()
    time_web_token = serializers.CharField()
    avito_client_id = serializers.CharField()
    avito_client_secret = serializers.CharField()
    bucket = serializers.CharField()

    def __init__(self, user: User, data: dict) -> None:
        self.__user = user
        super().__init__(data=data)

    def create(self, validated_data: dict) -> Project:
        return self.__user.project_set.create(
            name=validated_data['name'],
            status=Project.Status.ACTIVE,
            sheet_id="12345", # TODO generate normally
            xml_id="12345", # TODO generate normally
            time_web_token=validated_data['time_web_token'],
            avito_client_id=validated_data['avito_client_id'],
            avito_client_secret=validated_data['avito_client_secret'],
            bucket=validated_data['bucket']
        )
