from rest_framework import serializers

from studentarchives.models import StudentArchives


class StudentArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentArchives
        fields = '__all__'
        read_only_fields = ('created_date', 'modified_date')
