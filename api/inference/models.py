from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

def load_pipeline(model_repo: str) -> TextClassificationPipeline:
    tokenizer = AutoTokenizer.from_pretrained(model_repo)
    model = AutoModelForSequenceClassification.from_pretrained(model_repo)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer)

toxic_classifier = load_pipeline("framonmar7/toxic-classifier")
insult_classifier = load_pipeline("framonmar7/insult-classifier")
hate_classifier = load_pipeline("framonmar7/hate-classifier")
