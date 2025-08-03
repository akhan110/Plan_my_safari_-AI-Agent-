from crewai import Crew, Process
from agents import researcher, meteorologist, logistics_expert, trip_planner
from tasks import task_research, task_weather, task_visa, task_itinerary

# Create the Crew
crew = Crew(
    agents=[researcher, meteorologist, logistics_expert, trip_planner],
    tasks=[task_research, task_weather, task_visa, task_itinerary],
    process=Process.sequential,  # Run tasks one after another
    verbose=2  # Show step-by-step execution
)
