from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self) -> dict:
        duration = (self.leaved_at - self.entered_at).seconds
        hours = duration // 3600

        minutes = (duration % 3600) // 60

        passcard_duration = f'{hours}ч {minutes}мин'

        durations = {
            'passcard_duration': passcard_duration
        }

        return durations

    def is_long(self, minutes=60):
        flag = True
        if self.leaved_at:
            duration = (self.leaved_at - self.entered_at).seconds / 60
            flag = duration >= minutes

        return flag