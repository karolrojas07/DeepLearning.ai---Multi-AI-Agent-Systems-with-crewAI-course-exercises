from .crew import EventPlanningCrew
import warnings
from IPython.display import Markdown

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'event_topic': "Tech Innovation Conference",
        'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
        'event_city': "San Francisco",
        'tentative_date': "2024-09-15",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Conference Hall"
    }
    
    try:
        result = EventPlanningCrew().crew().kickoff(inputs=inputs)
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    
if __name__ == "__main__":
    run()