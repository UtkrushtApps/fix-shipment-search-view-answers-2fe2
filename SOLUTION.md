# Solution Steps

1. Open `tracker/views.py` and replace the direct `request.GET["tracking_code"]` lookup with `request.GET.get('tracking_code', '').strip()` so missing keys and whitespace-only input do not raise a `KeyError`.

2. Add an early validation branch: if the tracking code is empty after stripping whitespace, render `tracker/tracking_result.html` with a friendly `error_message` such as `Please enter a tracking code.`.

3. Query the database safely without allowing an unhandled exception. Use `Shipment.objects.filter(code=tracking_code).first()` instead of `.get(...)`, or catch `Shipment.DoesNotExist` explicitly.

4. If no shipment is found, render the same `tracking_result.html` template with a friendly not-found message that includes the words `not found`, and do not raise an exception.

5. If a shipment is found, render the template with the object under the context key `shipment` so the existing template can display `shipment.code`, `shipment.status`, and `shipment.courier_name`.

6. Do not change the template, model, or URL configuration. Keep the fix fully contained inside `search_shipment` so all scenarios return a normal HTTP 200 response rather than a Django debug error page.

7. Run migrations and test the page manually: visit `/shipments/search/?tracking_code=` for the empty case, `/shipments/search/?tracking_code=UNKNOWN` for the not-found case, and `/shipments/search/?tracking_code=TRK001` or `TRK002` for successful rendering.

