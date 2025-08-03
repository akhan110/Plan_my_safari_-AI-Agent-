from crewai import Task
from agents import researcher, meteorologist, logistics_expert, trip_planner

# Task 1: Research top locations and cultural experiences
task_research = Task(
    description="Find the best safari parks, beaches, and cultural experiences in Tanzania based on the user's trip request.",
    expected_output="A list of recommended destinations and activities.",
    agent=researcher
)

# Task 2: Provide weather forecast for target destinations
task_weather = Task(
    description="Get current and upcoming weather information for Tanzanian locations relevant to the user's trip request.",
    expected_output="Weather summary and suggestions for best times to visit.",
    agent=meteorologist
)

# Task 3: Visa and health guidance
task_visa = Task(
    description=(
        "Provide visa guidance for travel to Tanzania including:\n"
        "- Visa types (eVisa, on-arrival, embassy)\n"
        "- Application process and required documents\n"
        "- Visa fees and validity\n"
        "- Health/vaccination requirements\n"
        "- USD to Tanzanian Shilling exchange rate"
    ),
    expected_output=(
        "Detailed visa guide with requirements, methods, health guidelines, and real-time currency exchange info."
    ),
    agent=logistics_expert
)

# Task 4: Itinerary generation based on duration
task_itinerary = Task(
    description=(
        "Using the outputs from other tasks, create a complete {trip_duration} travel itinerary in Tanzania. "
        "It should include:\n"
        "- Daily activities for the entire duration\n"
        "- Weather considerations per location\n"
        "- Visa details (type + how to obtain it)\n"
        "- Currency exchange (USD to TZS)\n"
        "- Cultural tips and safety suggestions"
    ),
    expected_output=(
        "A customized itinerary for {trip_duration} with:\n"
        "- Daily breakdown of activities\n"
        "- Weather and packing guidance\n"
        "- Visa/currency info\n"
        "- Cultural dos and don'ts"
    ),
    agent=trip_planner,
    context=[task_research, task_weather, task_visa]
)
