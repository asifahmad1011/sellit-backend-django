from rest_framework import serializers

from studentarchives.models import StudentArchives


class StudentArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentArchives
        fields = ['matrikel_number', 'first_name', 'last_name', 'dob', 'email', 'address', 'phone_number',
                  'postal_code', 'created_date', 'modified_date']
