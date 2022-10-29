from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in not_leaved:
        visit_content = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': visit.format_duration(),
                'is_strange': visit.is_long()
            }
        non_closed_visits.append(visit_content)


    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
