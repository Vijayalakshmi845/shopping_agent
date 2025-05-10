# shopping_agent
Here's a `README.md` file for your **AI Shopping Assistant** project using Cohere:

---

```markdown
# 🛒 AI Shopping Assistant using Cohere

This Python script acts as a simple **AI-powered shopping assistant**. It takes your shopping preferences as input and uses **Cohere's language model** to generate a list of 5 product recommendations along with short descriptions.

---

## 📌 Features

- Accepts natural language input about what you want to shop for
- Uses Cohere's `command-r-plus` model for smart, contextual product suggestions
- Outputs concise descriptions for each recommended item
- Easy to run via the command line

---

## 🧪 Example

```

What are you looking to buy? wireless earbuds

🛒 Recommended Products:

1. SoundCore Liberty Air 2 Pro – Noise-cancelling earbuds with rich sound and customizable EQ.
2. Jabra Elite 75t – Compact, secure-fit earbuds with strong bass and long battery life.
3. Sony WF-1000XM4 – Premium noise-canceling earbuds with LDAC support and long playtime.
4. Samsung Galaxy Buds 2 – Affordable option with balanced audio and seamless Samsung integration.
5. Apple AirPods Pro – Well-rounded earbuds with spatial audio and tight integration with iOS.

````

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-shopping-assistant.git
cd ai-shopping-assistant
````

### 2. Install Dependencies

```bash
pip install cohere
```

### 3. Set Up API Key

Open the script and replace the placeholder with your actual Cohere API key:

```python
co = cohere.Client('your_api_key_here')
```

🔐 **Optional Security Tip**: Use environment variables for API key:

```python
import os
co = cohere.Client(os.getenv("COHERE_API_KEY"))
```

---

## 💻 Run the Script

```bash
python shopping_assistant.py
```

Then enter your shopping query when prompted.

---

## 🔒 Security Note

Do **NOT** expose your API key in public repositories. Use a `.env` file or environment variables in production.

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 🤖 Powered by

* [Cohere AI](https://cohere.com)

```

---

Would you like help adding `.env` support or converting this into a Streamlit app for a web UI?
```
