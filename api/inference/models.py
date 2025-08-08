from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

toxic_classifier = None
insult_classifier = None
hate_classifier = None

def load_pipeline(model_repo: str) -> TextClassificationPipeline:
    tokenizer = AutoTokenizer.from_pretrained(model_repo)
    model = AutoModelForSequenceClassification.from_pretrained(model_repo)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer)

def load_all_models():
    global toxic_classifier, insult_classifier, hate_classifier
    toxic_classifier = load_pipeline("framonmar7/toxic-classifier")
    insult_classifier = load_pipeline("framonmar7/insult-classifier")
    hate_classifier = load_pipeline("framonmar7/hate-classifier")
