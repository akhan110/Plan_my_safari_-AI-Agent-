from crewai import Agent
from tools import TanzaniaSearchTool, TanzaniaWeatherTool, TanzaniaVisaTool
from config import get_llm

# Load selected LLM
try:
    llm = get_llm()
except ValueError as e:
    raise ValueError(f"Failed to initialize LLM: {str(e)}")

# Initialize tools
search_tool = TanzaniaSearchTool()
weather_tool = TanzaniaWeatherTool()
visa_tool = TanzaniaVisaTool()

# Define agents
researcher = Agent(
    role="Tanzania Travel Specialist",
    goal="Find the best safari parks, beaches, and cultural experiences",
    backstory="Expert in African travel with 5+ years of experience.",
    tools=[search_tool],  # Pass as a list of instantiated tools
    llm=llm,
    verbose=True,
    allow_delegation=False  # Optional: Prevent delegation if not needed
)

meteorologist = Agent(
    role="Tanzania Climate Expert",
    goal="Provide weather forecasts and seasonal travel advice",
    backstory="Former safari guide with deep knowledge of Tanzanian climates.",
    tools=[weather_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

logistics_expert = Agent(
    role="Immigration and Finance Advisor",
    goal="Help travelers understand visa, currency, and health requirements",
    backstory="Worked with Tanzanian embassies and finance departments.",
    tools=[visa_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

trip_planner = Agent(
    role="Travel Itinerary Designer",
    goal="Create tailored itineraries for Tanzanian trips",
    backstory="Award-winning East Africa travel consultant.",
    tools=[search_tool, visa_tool, weather_tool],  # Include all relevant tools
    llm=llm,
    verbose=True,
    allow_delegation=True  # Allow delegation to other agents
)