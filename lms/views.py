from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lms.models import Course, Lesson, CourseSubscription
from lms.paginators import CoursePaginator, LessonPaginator
from lms.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, CourseSubscribeSerializer
from users.models import Payment
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
        elif self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModerator | IsOwner,)
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsModerator | IsOwner,)
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsModerator | IsOwner,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsModerator | IsOwner,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (~IsModerator | IsOwner,)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_mode')
    ordering_fields = ('payment_date',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSubscribeSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)

    def perform_create(self, serializer):
        subscribe = serializer.save()
        subscribe.user = self.request.user
        subscribe.save()

    # def post(self, request, *args, **kwargs):
    #     user = self.request.user
    #     course_id = self.request.data.get('course_id')
    #     course_item = get_object_or_404(Course, id=course_id)
    #     subs_item = CourseSubscription.objects.filter(user=user, course=course_item)
    #     if subs_item.exists():
    #         subs_item.delete()
    #         message = 'подписка удалена'
    #     else:
    #         CourseSubscription.objects.filter(user=user, course=course_item)
    #         message = 'подписка добавлена'
    #
    #     return Response({"message": message})


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = CourseSubscribeSerializer
    queryset = CourseSubscription.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = CourseSubscription.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)
