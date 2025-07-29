# Text-Analysis-with-Azure-AI-Language

## Description

The Text Analysis Web App is an intelligent application designed to perform comprehensive text analytics using Azure AI Language services. Users can input any text, and the application will return deep insights, including language detection, sentiment analysis, key phrases, and recognized entities.
Built with a Flask backend, this app demonstrates how to seamlessly integrate powerful cloud-based AI to analyze unstructured text. It serves as a practical example for developers looking to incorporate natural language processing (NLP) into their applications for tasks like content moderation, customer feedback analysis, and information extraction.


---

## Features
- Language Detection: Automatically identifies the language of the input text.
- Sentiment Analysis: Determines if the text's sentiment is positive, negative, or neutral.
- Key Phrase Extraction: Pulls out the most important topics and phrases.
- Entity Recognition: Identifies and categorizes named entities (e.g., people, places, organizations).
- Linked Entity Recognition: Recognizes well-known entities and provides links to their Wikipedia pages.


---

##  Tech Stack
- **Python 3.11+**
- **Flask** (for the web interface)
- **Azure AI Language Service API**


--- 

##  Project Structure
```
├── app.py                     # Flask web application
├── text_analysis.py           # CLI script to test Azure Custom Vision predictions
├── templates/
│   └── index.html             # Web interface template
├── static/
│   └── style.css              # Web style template
├── requirements.txt 
├── README.md                    
└── LICENSE                    


```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/JoshuaFerando/Text-Analysis-with-Azure-AI-Language
cd Text-Analysis-with-Azure-AI-Language
```

### 2. Install Dependencies
Using **pip**:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Azure AI Language Setup
1. Create a Language Service resource in the Azure portal.
2. Once created, navigate to the Keys and Endpoint section of your resource.
3. Get the following credentials:
   - **Service Endpoint**
   - **API Key**
 
4. Add these to your environment variables:
   ```bash
   
    AI_SERVICE_ENDPOINT="YOUR_AZURE_ENDPOINT"
    AI_SERVICE_KEY="YOUR_AZURE_API_KEY"

   ```

---

## Running the Web App
```bash
python app.py
```
Then open your browser and navigate to:
```
http://localhost:5000
```

---

## Deployment
You can deploy this project to:
- **Azure App Service**
- **Replit**
- **Heroku**
- **Any cloud hosting that supports Flask**

---

## License
This project is licensed under the **Apache-2.0 license**.

---

### 👨‍💻 Author
Developed by **Joshua Fernando**  
Feel free to contribute or open issues!

