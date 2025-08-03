import requests
import os
from langchain_core.tools import BaseTool
from typing import Optional, Type

# ------------------------------
# Tool 1: Tanzania Travel Search
# ------------------------------
class TanzaniaSearchTool(BaseTool):
    name: str = "TanzaniaSearch"
    description: str = "Searches for Tanzania travel info from official government or tourism sources."

    def _run(self, query: str) -> str:
        if not query:
            return "Error: Query cannot be empty."
        
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Error: TAVILY_API_KEY environment variable not set."

        try:
            response = requests.post(
                "https://api.tavily.com/search",
                json={
                    "query": f"{query} site:.tz OR site:tanzaniatourism.go.tz",
                    "include_answer": True,
                    "max_results": 3,
                    "api_key": api_key
                },
                timeout=10
            )
            response.raise_for_status()  # Raise an exception for bad HTTP status
            results = response.json()
            if not results.get("results"):
                return "No results found for the query."
            return "\n".join(
                f"{i+1}. {res['title']}\n{res['content']}\n{res['url']}"
                for i, res in enumerate(results.get("results", []))
            )
        except requests.RequestException as e:
            return f"Search error: {str(e)}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async search not supported.")

# ------------------------------
# Tool 2: Weather Tool
# ------------------------------
class TanzaniaWeatherTool(BaseTool):
    name: str = "TanzaniaWeather"
    description: str = "Gets current weather for Tanzanian cities or regions."

    def _run(self, location: str = "Dar es Salaam") -> str:
        if not location:
            return "Error: Location cannot be empty."

        try:
            url = f"https://wttr.in/{location}?format=%C+%t+%h+%w"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return f"Weather in {location}: {response.text.strip()}"
        except requests.RequestException as e:
            return f"Weather data unavailable: {str(e)}"

    async def _arun(self, location: str) -> str:
        raise NotImplementedError("Async weather lookup not supported.")

# ------------------------------
# Tool 3: Visa & Currency Tool
# ------------------------------
class TanzaniaVisaTool(BaseTool):
    name: str = "VisaInfo"
    description: str = "Provides visa, currency exchange, and vaccination requirements for Tanzania."

    def _run(self, query: Optional[str] = None) -> str:
        try:
            info = {
                "currency": "Tanzanian Shilling (TZS). Exchange rate: ~2500 TZS per USD.",
                "visa": "Most travelers need a visa ($50–$100). Apply at https://eservices.immigration.go.tz/visa/",
                "health": "Yellow fever certificate required if traveling from an endemic country."
            }
            if query:
                return info.get(query.lower(), "Query not found. Available options: currency, visa, health.")
            return "\n".join(info.values())
        except Exception as e:
            return f"Visa info unavailable: {str(e)}"

    async def _arun(self, query: Optional[str] = None) -> str:
        raise NotImplementedError("Async visa info lookup not supported.")