from .crew import JobApplicationCrew
import warnings

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
        'job_posting_url': 'https://jobs.lever.co/AIFund/b9cd61ea-cae1-411a-987f-ea40ea6f7db8',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an MBA and a strong
        background in AI and data science. Noah has successfully led
        major tech initiatives and startups, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach."""
    }
    
    try:
        result = JobApplicationCrew().crew().kickoff(inputs=inputs)
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    
if __name__ == "__main__":
    run()