from crew import crew

def main():
    # You can change this to test different inputs
    trip_request = "Family safari and beach vacation for 2 adults and 2 kids"
    trip_duration = "3 days"  # Try "3 days", "7 days", "1 month", etc.

    print("Generating travel itinerary...\n")
    
    result = crew.kickoff(
        inputs={
            "trip_request": trip_request,
            "trip_duration": trip_duration
        }
    )

    print("\n===== FINAL ITINERARY =====\n")
    print(result)

if __name__ == "__main__":
    main()
