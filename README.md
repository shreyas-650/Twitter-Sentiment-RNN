# 🐦 Tweet Sentiment Analysis

A deep learning-based NLP application that classifies tweets into **Negative, Neutral, or Positive** sentiment using a trained TensorFlow/Keras model. The application provides a simple, interactive interface built with Streamlit.

## 🚀 Features

- **Sentiment Classification:** Predicts whether a tweet expresses negative, neutral, or positive sentiment.
- **Deep Learning:** Uses a pre-trained TensorFlow/Keras model.
- **Text Processing:** Converts tweets into token sequences and pads them to a fixed length of 100 tokens.
- **Interactive Interface:** Provides a simple Streamlit interface for entering tweets and viewing predictions.
- **Fast Predictions:** Generates sentiment predictions using the trained model.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **TensorFlow / Keras** — Deep learning and model inference
- **NumPy** — Numerical operations and predicted-class selection
- **Streamlit** — Interactive web application
- **Pickle** — Loading the saved tokenizer

## 📁 Project Structure

```text
Tweet-Sentiment-RNN/
│
├── app.py              # Streamlit application
├── model.h5            # Trained TensorFlow/Keras model
├── tokenizer.pkl       # Saved text tokenizer
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 🧠 How It Works

1. **Input:** Enter a tweet in the Streamlit text area.
2. **Tokenization:** The saved tokenizer converts the tweet into a sequence of integer token IDs.
3. **Padding:** The sequence is padded to 100 tokens using post-padding.
4. **Prediction:** The trained deep learning model generates class probabilities.
5. **Classification:** NumPy's `argmax()` selects the class with the highest probability.
6. **Output:** The predicted sentiment is displayed in the interface.

### Sentiment Labels

| Predicted Class | Sentiment |
|---:|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

The label mapping must match the class encoding used during model training.

## 📦 Required Files

- `app.py` — Application source code
- `model.h5` — Trained model used for predictions
- `tokenizer.pkl` — Tokenizer fitted during training
- `requirements.txt` — Required Python packages

**Important:** The model and tokenizer must come from the same training pipeline. The tokenizer, sequence length, padding configuration, and class mapping should match those used during training.

## 🔮 Future Improvements

- Display confidence scores for each sentiment.
- Add batch sentiment analysis for multiple tweets.
- Improve text preprocessing and handling of emojis, hashtags, and slang.
- Evaluate and improve performance on unseen tweets.
- Deploy the application online for public access.

## 👨‍💻 Author

**Shreyas Singh**

GitHub: [Shreyas Singh](https://github.com/shreyas-650)

---

*Built with Python, TensorFlow, and Streamlit to explore deep learning and natural language processing for sentiment classification.*