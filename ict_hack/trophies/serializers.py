from rest_framework import serializers

from achievements.models import Achievement
from events.enums import EventCategory, EventStatus
from trophies.models import Trophy, Trophies
from users.models import User


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = ('code', 'name', 'description', 'category', 'has_trophy')

    has_trophy = serializers.SerializerMethodField(method_name='check_has_trophy')

    def check_has_trophy(self, obj) -> bool:
        request = self.context.get('request')
        user = request.user if request else None

        get_count = lambda category: Achievement.objects.filter(
            event__category=category, event__status=EventStatus.REPORT_ACCEPTED, user=user).count()

        rules = {
            Trophies.EDUCATION_5:  get_count(EventCategory.EDUCATION) >= 5,
            Trophies.EDUCATION_10: get_count(EventCategory.EDUCATION) >= 10,
            Trophies.SCIENCE_5:    get_count(EventCategory.SCIENCE) >= 5,
            Trophies.SCIENCE_10:   get_count(EventCategory.SCIENCE) >= 10,
            Trophies.SOCIAL_5:     get_count(EventCategory.SOCIAL) >= 5,
            Trophies.SOCIAL_10:    get_count(EventCategory.SOCIAL) >= 10,
            Trophies.CULTURE_5:    get_count(EventCategory.CULTURE) >= 5,
            Trophies.CULTURE_10:   get_count(EventCategory.CULTURE) >= 10,
            Trophies.SPORT_5:      get_count(EventCategory.SPORT) >= 5,
            Trophies.SPORT_10:     get_count(EventCategory.SPORT) >= 10,
            Trophies.PGAS_TOP3:    User.objects.filter(is_staff=False, pk=user.pk).order_by('-pgas_score')[:3].exists(),
        }

        if obj.code in rules:
            return rules[obj.code]
        return False
