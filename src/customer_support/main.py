from .crew import CustomerSupportCrew
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
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew and kicking it off, specifically how can I add memory to my crew? Can you provide guidance?"
    }
    
    try:
        result = CustomerSupportCrew().crew().kickoff(inputs=inputs)
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    
if __name__ == "__main__":
    run()