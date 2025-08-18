# This Project is made of Langcahin can be useful in using different models and differnt tyoes of chat bot's as well

# Agentic AI Chatbot with Groq and Tavily  

This project demonstrates how to build **agentic AI applications** starting from a simple Python foundation. The chatbot is powered by **Groq open-source models** and extended with the **Tavily API** for web-enabled search and real-time data fetching.  

It includes:  
- A **basic chatbot** directly connected to an LLM  
- A **web-enabled chatbot** that fetches and summarizes real-world information  
- An **AI news summarization tool** with daily, weekly, and monthly updates  

---

## 🚀 Features  

### 1. Basic Chatbot  
Uses Groq LLMs to answer simple queries.  
Example: A basic question on *machine learning*.  

<img width="1919" height="1079" alt="Screenshot 2025-08-18 192355" src="https://github.com/user-attachments/assets/bc017804-d848-4177-8d46-d7ad7f8db4b0" />


---

### 2. Web-Enabled Chatbot  
Integrates the Tavily API to perform live searches.  
Tested by searching my own name, showcasing real-time data retrieval.  

<img width="1919" height="1079" alt="Screenshot 2025-08-18 192533" src="https://github.com/user-attachments/assets/52e30339-0340-4bb7-be69-7df263681c40" />


---

### 3. AI News Summarization  
Automatically generates summaries of AI news with daily, weekly, and monthly frequencies.  

- **Daily AI News**  
<img width="1914" height="1079" alt="Screenshot 2025-08-18 192808" src="https://github.com/user-attachments/assets/4d9369a1-d88b-443f-abed-0f495c052344" />


- **Weekly AI News**  
<img width="1919" height="1018" alt="Screenshot 2025-08-18 192633" src="https://github.com/user-attachments/assets/ed5c09ee-b492-43e7-88ea-bb1c3fddbfe6" />


- **Monthly AI News**  
<img width="1919" height="1021" alt="Screenshot 2025-08-18 192707" src="https://github.com/user-attachments/assets/d78899ab-232c-483e-9220-6f1888f552c6" />


---

## 🛠️ Tech Stack  

- **Python**  
- **LangGraph**  
- **Groq LLMs**   
- **Tavily API** for real-time search  
- **Streamlit** for UI  

---

## 📂 Project Structure  

├── app.py # Main Streamlit application
├── requirements.txt # Project dependencies
├── utils/ # Utility functions
│ ├── chatbot.py # LLM chatbot logic
│ ├── web_agent.py # Web-enabled chatbot with Tavily
│ └── news_agent.py # AI news summarization
└── README.md # Project documentation



---

## ⚙️ Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/agentic-ai-chatbot.git
   cd agentic-ai-chatbot
   
2.install dependencides:

pip install -r requirements.txt

3.Add api_keys:

export GROQ_API_KEY="your_groq_api_key"

export TAVILY_API_KEY="your_tavily_api_key"

4.Run the Application:

streamlit run app.py



🙌 Acknowledgements

Groq for open-source LLMs

Tavily for real-time search APIs

LangChain / LangGraph for building agentic AI workflows

Special thanks to Krish Naik for mentorship and guidance

