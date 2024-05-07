from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms.models import Lesson, Course, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user3@mail.com", password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Test course", description="Test course")
        self.lesson = Lesson.objects.create(title="Test lesson", description="Test lesson",
                                            video_link="https://youtube.com/", course=self.course, owner=self.user)

    def test_create_lesson(self):
        url = reverse("lms:lesson-create")
        data = {
            "title": "Test lesson",
            "description": "Test lesson",
            "video_link": "https://youtube.com/",
            "course": self.course.pk,
            "owner": self.user.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertTrue(Lesson.objects.all().exists())

    def test_lesson_list(self):
        url = reverse("lms:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview": None,
                    "video_link": "https://youtube.com/",
                    "course": self.course.id,
                    "owner": self.user.pk
                }
            ]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson-lesson", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_update(self):
        url = reverse("lms:lesson-update", args=(self.lesson.pk,))
        data = {
            "title": "Update test lesson",
            "description": "Update test lesson",
            "video_link": "https://youtube.com/"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Update test lesson")

    def test_lesson_delete(self):
        url = reverse("lms:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user3@mail.com", password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Test course", description="Test course")
        self.lesson = Lesson.objects.create(title="Test lesson", description="Test lesson", course=self.course)
        self.subscription = CourseSubscription.objects.create(owner=self.user, course=self.course)

    def test_create_subscription(self):
        url = reverse("lms:subscription_create")
        data = {
            "owner": self.user.pk,
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 1)
        self.assertTrue(Lesson.objects.all().exists())

    def test_subscription_delete(self):
        url = reverse("lms:subscription_delete", args=(self.subscription.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CourseSubscription.objects.all().count(), 0)

    def test_subscription_list(self):
        url = reverse("lms:subscription_list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.subscription.pk,
                "is_subscribe": False,
                "owner": self.user.pk,
                "course": self.course.pk
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
