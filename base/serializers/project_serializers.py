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

    __sheet_id: str | None = None

    def __init__(self, user: User, data: dict) -> None:
        self.__user = user
        super().__init__(data=data)

    def set_sheet_id(self, sheet_id: str) -> None:
        self.__sheet_id = sheet_id

    def create(self, validated_data: dict) -> Project:
        if self.__sheet_id is None:
            raise ValueError('You must set client sheet id')

        return self.__user.project_set.create(
            name=validated_data['name'],
            status=Project.Status.ACTIVE,
            sheet_id=self.__sheet_id,
            xml_id=self.__sheet_id,
            time_web_token=validated_data['time_web_token'],
            avito_client_id=validated_data['avito_client_id'],
            avito_client_secret=validated_data['avito_client_secret'],
            bucket=validated_data['bucket']
        )
