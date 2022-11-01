from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcards = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcards)

    passcard_visits = []

    for visit in visits:
        visit_content = {
                'entered_at': visit.entered_at,
                'duration': visit.format_duration(),
                'is_strange': visit.is_long()
            }
        passcard_visits.append(visit_content)
    
    context = {
        'passcard': passcards,
        'this_passcard_visits': passcard_visits
    }

    return render(request, 'passcard_info.html', context)