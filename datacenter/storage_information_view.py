from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    local_time = localtime()
    
    dutation = local_time - visit

    return dutation.seconds


def format_duration(duration):
    # TODO пишите код здесь
    hours = duration // 3600

    minutes = (duration % 3600) // 60

    return f'{hours}ч {minutes}мин'


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)

    visit = Visit.objects.all()[0]

    duration = get_duration(not_leaved[0].entered_at)

    non_closed_visits = [
        {
            'who_entered': not_leaved[0].passcard,
            'entered_at': not_leaved[0].entered_at,
            'duration': format_duration(duration),
            'is_strange': Visit.is_long(visit)
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
