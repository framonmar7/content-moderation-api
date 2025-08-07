from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema
from api.inference.models import toxic_classifier, insult_classifier, hate_classifier
from api.docs.schemas import input_schema, responses

def classify_text(request, classifier):
    text = request.data.get("text")
    if not text:
        return Response(
            {"error": "Missing 'text' field in request body."},
            status=HTTP_400_BAD_REQUEST
        )
    result = classifier(text)[0]
    return Response(result)

def register_endpoint(name, classifier, summary):
    @swagger_auto_schema(
        method='post',
        operation_id=name,
        operation_summary=summary,
        request_body=input_schema,
        responses=responses,
        tags=["Classification"]
    )
    @api_view(["POST"])
    def view(request):
        return classify_text(request, classifier)
    return view

classify_toxic = register_endpoint("classifyToxic", toxic_classifier, "Classify toxic language")
classify_insult = register_endpoint("classifyInsult", insult_classifier, "Classify insulting language")
classify_hate = register_endpoint("classifyHate", hate_classifier, "Classify hate speech")
