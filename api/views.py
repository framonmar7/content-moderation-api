from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inference.models import toxic_classifier, insult_classifier, hate_classifier

def classify_text(request, classifier):
    text = request.data.get("text")
    if not text:
        return Response({"error": "Missing 'text' field in request body."}, status=status.HTTP_400_BAD_REQUEST)
    result = classifier(text)[0]
    return Response(result)

@api_view(["POST"])
def classify_toxic(request):
    return classify_text(request, toxic_classifier)

@api_view(["POST"])
def classify_insult(request):
    return classify_text(request, insult_classifier)

@api_view(["POST"])
def classify_hate(request):
    return classify_text(request, hate_classifier)
