from django.db import migrations


def seed_shipments(apps, schema_editor):
    Shipment = apps.get_model('tracker', 'Shipment')
    Shipment.objects.create(code='TRK001', status='In Transit', courier_name='FastShip Logistics')
    Shipment.objects.create(code='TRK002', status='Delivered', courier_name='QuickMove Co.')
    Shipment.objects.create(code='TRK003', status='Pending Pickup', courier_name='CityRun Express')


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_shipments, migrations.RunPython.noop),
    ]
