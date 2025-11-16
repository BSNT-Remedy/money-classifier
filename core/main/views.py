from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from .models import Prediction

def index(request):
    return render(request, 'main/index.html')

def analytics(request):
    return render(request, 'main/analytics.html')



@require_POST
def save_prediction(request):
    """
    Accept JSON { label: str, confidence: float } and save.
    CSRF token must be sent (the JS below will do that).
    """
    try:
        data = json.loads(request.body)
        label = data.get('label')
        confidence = float(data.get('confidence', 0))
    except (ValueError, json.JSONDecodeError, TypeError):
        return HttpResponseBadRequest("Invalid JSON")

    if not label:
        return HttpResponseBadRequest("Missing label")

    user = request.user if request.user.is_authenticated else None
    pred = Prediction.objects.create(user=user, label=label, confidence=confidence)
    return JsonResponse({
        "status": "ok",
        "id": pred.id,
        "label": pred.label,
        "confidence": pred.confidence
    })


@require_GET
def predictions_stats(request):
    """
    Return JSON with counts per label and average confidence:
    { labels: [...], counts: [...], avg_confidence: {...} }
    """
    qs = Prediction.objects.all()
    # Optionally filter by date/user query params (not required)
    group = qs.values('label').annotate(count=Count('id'), avg_conf=Avg('confidence')).order_by('-count')

    labels = [g['label'] for g in group]
    counts = [g['count'] for g in group]
    avg_confidence = { g['label']: float(g['avg_conf']) for g in group }

    return JsonResponse({
        "labels": labels,
        "counts": counts,
        "avg_confidence": avg_confidence,
        "total": qs.count()
    })