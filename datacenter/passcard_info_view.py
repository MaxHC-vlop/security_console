from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def format_duration(duration):
    hours = duration // 3600

    minutes = (duration % 3600) // 60

    return f'{hours}ч {minutes}мин'


def passcard_info_view(request, passcode):
    obj = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=obj)
    this_passcard_visits = []
    for visit in visits:
        duration = visit.leaved_at - visit.entered_at

        qwe = format_duration(duration.seconds)

        visit_content = {
                'entered_at': visit.entered_at,
                'duration': qwe,
                'is_strange': Visit.is_long(visit)
            }
        this_passcard_visits += [visit_content]
    
    context = {
        'passcard': obj,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)