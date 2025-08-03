# 🦁 Safari Travel Tools — AI-Powered Safari Assistant 🌍

![Demo](demo%20image.png)

This project provides a set of intelligent tools for planning safaris in East Africa (with a focus on Tanzania) using AI and real-time APIs. It combines domain-filtered travel search, location-based weather, and visa/currency/health tools into a single set of Python utilities for agents.

---

## ✨ Features

- 🔍 **Safari-Focused Travel Search**  
  Search for safari-related travel information using the Tavily Search API with filters for Tanzanian domains (`.tz`, `tanzaniatourism.go.tz`). The tool returns the top 3 relevant results including snippets and URLs.

- ☁️ **Weather for Safari Locations**  
  Automatically extracts safari park or city names from the search results and fetches the current weather for each using [wttr.in](https://wttr.in). Supports multiple locations per search.

- 📄 **Visa, Currency & Health Guidelines**  
  Get quick access to static but essential safari traveler information:
  - Visa process, online application link, and cost
  - Currency (Tanzanian Shilling - TZS), exchange advice, and card usage
  - Health precautions including vaccinations and malaria risk

---

## 🧠 How It Works

- **Search Tool**: Uses Tavily API with region/domain filter to fetch local safari-related results.
- **Location Extraction**: Parses the titles and content of search results to find probable safari cities/locations using simple regex.
- **Weather Fetching**: Queries weather for up to 5 unique cities using the wttr.in HTTP API.
- **Visa Tool**: Returns visa, currency, and health info based on keyword query (`"visa"`, `"currency"`, or `"health"`).

---

## 🛠️ Tech Stack

- Python 3
- [LangChain](https://www.langchain.com/)
- [Tavily Search API](https://www.tavily.com/)
- [wttr.in weather API](https://wttr.in/)
- Regex-based location detection

---

## 🚀 Use Cases

- Integrate with CrewAI or LangChain agents for safari trip planning
- Add to a travel chatbot or voice assistant for safari inquiries
- Use as a lightweight tool for educational or prototyping purposes

---

## 🔑 Setup Instructions

**Clone the repository**
   ```bash
   git clone https://github.com/your-username/Plan_my_safari_-AI-Agent-.git
   cd Plan_my_safari_-AI-Agent-
