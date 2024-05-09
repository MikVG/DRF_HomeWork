from rest_framework import serializers

from lms.models import Course, Lesson, CourseSubscription
from lms.validators import VideoLinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(link='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_subscription(self, instance):
        if self.context['request'].user == instance.owner:
            return True
        return False


class CourseSubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSubscription
        fields = '__all__'
