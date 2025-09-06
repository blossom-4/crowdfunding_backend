from rest_framework import serializers
from django.apps import apps

class CaseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = apps.get_model('cases.Case')
        fields = '__all__'


class JudgementSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = apps.get_model('cases.Judgement')
        fields = '__all__'

class JudgementDetailSerializer(JudgementSerializer):
    def update(self, instance, validated_data):
        instance.verdict = validated_data.get('verdict', instance.verdict)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.save()
        return instance


class CaseDetailSerializer(CaseSerializer):
    judgements = JudgementSerializer(many=True, read_only=True)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance