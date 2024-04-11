from architect import SolutionCrew
from textwrap import dedent
from utils.helpers import print_weights_nicely
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    print("## Welcome to Solution Architecture Crew")
    print('-------------------------------')
    problem = input(dedent("""What do you want to architect? Describe your business problem: """))

    cloud_provider = input("Select cloud provider [AWS(default)]: ") or "AWS"
    model_choice = input("Select model [OpenAI, Anthropic(default)]: ") or "Anthropic"

    weights = {
        "operational_excellence": 0.8,
        "security": 1,
        "reliability": 0.8,
        "performance_efficiency": 0.8,
        "cost_optimization": 0.5,
        "sustainability": 0.5
    }

    for pillar in weights:
        while True:
            try:
                user_input = input(f"Rate the importance of the '{pillar}' for your solution (0-100) Currently {int(weights[pillar]*100)}: ") or (weights[pillar]*100)
                importance = float(user_input) / 100
                if 0 <= importance <= 1:
                    weights[pillar] = importance
                    break
                else:
                    print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    print_weights_nicely(weights)

    if cloud_provider == "AWS":
        from agents.aws_agents import AWSAgents
        from tasks.aws_tasks import AWSTasks
        crew = SolutionCrew(problem,
                            weights,
                            cloud_provider,
                            model_choice,
                            openai_api_key=os.getenv("OPENAI_API_KEY"),
                            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
                            serper_api_key=os.getenv("SERPER_API_KEY"))
    else:
        print("Invalid cloud provider. Please select AWS, Azure, or GCP.")

    result = crew.run()
    print("\n\n")
    print("Solution Evaluation")
    print("---------------------\n")
    print(result)