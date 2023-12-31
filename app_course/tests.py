from django.urls import reverse
from rest_framework import status
from app_course.models import Subscription
from app_lesson.tests import LessonTestCase


class SubscriptionTestCase(LessonTestCase):

    def test_subscribe_unsubscribe_course(self):
        """Тестирование подписки на урок"""

        # Данные о пользователе для подписки на курс
        data = {
            'user': self.user.pk,
            # 'course': self.course.pk,
        }

        # Отправка запроса на подписку на курс
        response = self.client.post(reverse('app_course:subscribe', args=[self.course.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        # Проверка наличия подписки на курс
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), True)

        # Отправка запроса на отписку от курса
        response = self.client.delete(reverse('app_course:unsubscribe', args=[self.course.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

        # Проверка отсутствия подписки на курс
        self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), False)
