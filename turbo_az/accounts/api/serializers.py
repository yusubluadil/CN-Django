from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cars.models import Announcement


USER = get_user_model()

# required=False - Field adı verilməsə belə xəta verməyəcək.
# allow_null=True - Field adı mütləq verilməlidir, sadəcə null dəyər də qəbul edə bilir.
# write_only=True - Yalnız DB-yə əlavə olunduğu zaman məlumat ötürülməli field olur. Yəni, get sorğularında görünmür


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = USER
        fields = ('first_name', 'city', 'email', 'phone_number', 'password', 'confirm_password')

    def validate(self, attrs):
        pswd1 = attrs.get('password')
        pswd2 = attrs.pop('confirm_password')
        if pswd1 != pswd2:
            raise ValidationError({'detail': 'Daxil edilən şifrələr eyni deyil!'})

        attrs['password'] = make_password(pswd1)
        return super().validate(attrs)


class MeSerializer(serializers.ModelSerializer):
    # TODO: announcements sirf id gosterir onu duzelt
    announcements = serializers.PrimaryKeyRelatedField(
        queryset=Announcement.objects.all(), many=True
    )
    # city_name = serializers.SerializerMethodField()

    class Meta:
        model = USER
        fields = ('id', 'phone_number', 'first_name', 'email', 'city', 'announcements')

    # def get_announcements(self, obj):
    #     return obj.announcements.all()

    # def get_city_name(self, obj):
    #     return obj.
