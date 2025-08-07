# 🧠 Content Moderation API

This project is a RESTful API for automated moderation of user-generated content. It performs binary classification of text input to detect **toxic language**, **insults**, and **hate speech**.

## 🔬 Models

The API delegates inference to hosted models on Hugging Face Inference Endpoints. Each classifier is optimized for a specific moderation task:

- [Toxic Comment Classifier](https://huggingface.co/framonmar7/toxic-classifier) – Detects general toxicity.
- [Insult Comment Classifier](https://huggingface.co/framonmar7/insult-classifier) – Detects offensive or insulting language.
- [Hate Speech Classifier](https://huggingface.co/framonmar7/hate-classifier) – Detects hate speech or discriminatory language.

All models are finetuned on labeled datasets and are intended to be used as modular components of the moderation pipeline.

---

## 📚 Swagger Documentation

Interactive API documentation is automatically generated via **Swagger UI** and available at:

```
/swagger/
```

Each endpoint accepts a `POST` request with a JSON body containing a single `text` field.

Example:

```json
{
  "text": "You're worthless and stupid."
}
```

The response includes a `label` and a `score` (confidence).

---

## ⚙️ Setup Instructions

1. **Install the dependencies in a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. **Create your environment file**:

Copy the `.env.example` to `.env` and provide the values:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

3. **Prepare the backend**:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

4. **Run the development server**:

```bash
python manage.py runserver
```

Once the development server is running, you can access the application in your browser at the URL shown in the terminal.

---

## 🚦 Rate Limiting

To prevent abuse, the API uses `django-ratelimit` to limit excessive requests. Requests exceeding the threshold will receive HTTP 429 responses.

---

## 📜 License

This project is released under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it — with attribution.

---

## 👤 Author

Developed by [Francisco Jesús Montero Martínez](https://github.com/framonmar7)  
For suggestions, improvements, or collaboration, feel free to reach out.