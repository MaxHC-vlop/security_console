from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def format_duration(duration: int) -> str:
    hours = duration // 3600

    minutes = (duration % 3600) // 60

    return f'{hours}ч {minutes}мин'


def passcard_info_view(request, passcode):
    visitors = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=visitors)

    this_passcard_visits = []
    for visit in visits:
        duration = visit.leaved_at - visit.entered_at

        difference = format_duration(duration.seconds)

        visit_content = {
                'entered_at': visit.entered_at,
                'duration': difference,
                'is_strange': visit.is_long()
            }
        this_passcard_visits.append(visit_content)
    
    context = {
        'passcard': visitors,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)