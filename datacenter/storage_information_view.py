from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    local_time = localtime()
    
    dutation = local_time - visit

    return dutation.seconds


def format_duration(duration):
    hours = duration // 3600

    minutes = (duration % 3600) // 60

    return f'{hours}ч {minutes}мин'


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in not_leaved:

        duration = get_duration(visit.entered_at)

        visit_content = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': visit.is_long()
            }
        non_closed_visits.append(visit_content)


    context = {
        'non_closed_visits': non_closed_visits,
    }
    
    return render(request, 'storage_information.html', context)
