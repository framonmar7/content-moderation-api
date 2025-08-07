from drf_yasg import openapi

input_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["text"],
    properties={
        "text": openapi.Schema(
            type=openapi.TYPE_STRING,
            example="You are stupid and worthless."
        )
    }
)

output_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "label": openapi.Schema(
            type=openapi.TYPE_STRING,
            example="LABEL_1"
        ),
        "score": openapi.Schema(
            type=openapi.TYPE_NUMBER,
            format="float",
            example=0.93
        )
    }
)

bad_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "error": openapi.Schema(
            type=openapi.TYPE_STRING,
            example="Missing 'text' field in request body."
        )
    }
)

rate_limit_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "detail": openapi.Schema(
            type=openapi.TYPE_STRING,
            example="Rate limit exceeded."
        )
    }
)

responses = {
    200: openapi.Response("Successful classification", output_schema),
    400: openapi.Response("Bad request", schema=bad_request_schema),
    429: openapi.Response("Too many requests", schema=rate_limit_schema),
}
