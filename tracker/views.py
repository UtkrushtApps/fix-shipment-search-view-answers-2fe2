from django.shortcuts import render

from .models import Shipment


def search_shipment(request):
    tracking_code = request.GET.get('tracking_code', '').strip()

    if not tracking_code:
        return render(
            request,
            'tracker/tracking_result.html',
            {
                'error_message': 'Please enter a tracking code.',
            },
        )

    shipment = Shipment.objects.filter(code=tracking_code).first()

    if shipment is None:
        return render(
            request,
            'tracker/tracking_result.html',
            {
                'error_message': 'Shipment not found for the provided tracking code.',
            },
        )

    return render(
        request,
        'tracker/tracking_result.html',
        {
            'shipment': shipment,
        },
    )
