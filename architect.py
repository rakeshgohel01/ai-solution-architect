from crewai import Crew, Process
from crewai.task import TaskOutput
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


from textwrap import dedent
# from utils.callbacks import create_task_callback
from agents.aws_agents import AWSAgents
from tasks.aws_tasks import AWSTasks
from dotenv import load_dotenv

import os

load_dotenv()

def task_callback(output: TaskOutput, aspect: str, task_responses: dict):
    if task_responses is not None:
        task_responses[aspect] = output.raw_output

def create_task_callback(aspect: str, task_responses: dict = None):
    def callback(output: TaskOutput):
        task_callback(output, aspect, task_responses)
    return callback

class SolutionCrew:
    def __init__(self,
                 problem,
                 weights,
                 cloud_provider,
                 model_choice,
                 openai_api_key=None,
                 anthropic_api_key=None,
                 serper_api_key=None,
                 task_responses=None):
        self.problem = problem
        self.weights = weights
        self.task_responses = task_responses
        self.provider = cloud_provider
        self.model_choice = model_choice
        self.serper_api_key = serper_api_key
        self.openai_api_key = openai_api_key
        self.anthropic_api_key = anthropic_api_key

        if (cloud_provider == "AWS"):
            self.agents = AWSAgents(self.serper_api_key)
            self.tasks = AWSTasks()

        self.OpenAI35GPT = ChatOpenAI(
            model_name=os.getenv("OPENAI_MODEL_NAME"),
            openai_api_key=self.openai_api_key,
            temperature=0.7)
        self.Anthropic = ChatAnthropic(
            temperature=0.7,
            anthropic_api_key=self.anthropic_api_key,
            model_name=os.getenv("ANTHROPIC_MODEL_NAME"))

        if (model_choice == "OpenAI"):
            self.selectedllm = self.OpenAI35GPT
        else:
            self.selectedllm = self.Anthropic

    def run(self):
        solution_agent = self.agents.solution_agent(llm=self.selectedllm)
        evaluation_agent = self.agents.evaluation_agent(llm=self.selectedllm)
        operational_excellence_agent = self.agents.operational_excellence_agent(llm=self.selectedllm)
        security_agent = self.agents.security_agent(llm=self.selectedllm)
        reliability_agent = self.agents.reliability_agent(llm=self.selectedllm)
        performance_efficiency_agent = self.agents.performance_efficiency_agent(llm=self.selectedllm)
        cost_optimization_agent = self.agents.cost_optimization_agent(llm=self.selectedllm)
        sustainability_agent = self.agents.sustainability_agent(llm=self.selectedllm)

        solution_task = self.tasks.solution_task(
            agent=solution_agent,
            problem=self.problem,
            weights=self.weights,
            callback=create_task_callback("solution", self.task_responses)
        )
        operational_excellence_task = self.tasks.operational_excellence_task(
            operational_excellence_agent,
            self.problem,
            weights=self.weights,
            contextTasks=[solution_task],
            callback=create_task_callback("operational_excellence", self.task_responses)
        )
        security_task = self.tasks.security_task(
            security_agent,
            self.problem,
            weights=self.weights,
            contextTasks=[solution_task],
            callback=create_task_callback("security", self.task_responses)
        )
        reliability_task = self.tasks.reliability_task(
            reliability_agent,
            self.problem,
            weights=self.weights,
            contextTasks=[solution_task],
            callback=create_task_callback("reliability", self.task_responses)
        )
        performance_efficiency_task = self.tasks.performance_efficiency_task(
            performance_efficiency_agent,
            self.problem,
            weights=self.weights,
            contextTasks=[solution_task],
            callback=create_task_callback("performance_efficiency", self.task_responses)
        )
        cost_optimization_task = self.tasks.cost_optimization_task(
            cost_optimization_agent,
            self.problem,
            weights=self.weights,
            contextTasks=[solution_task],
            callback=create_task_callback("cost_optimization", self.task_responses)
        )
        sustainability_task = self.tasks.sustainability_task(
            sustainability_agent,
            self.problem,
            weights=self.weights,
            contextTasks=[solution_task],
            callback=create_task_callback("sustainability", self.task_responses)
        )
        evaluate_task = self.tasks.evaluate_task(
            evaluation_agent, self.problem,
            self.weights,
            callback=create_task_callback("evaluation", self.task_responses),
            contextTasks=[
                solution_task,
                operational_excellence_task,
                security_task, reliability_task,
                performance_efficiency_task,
                cost_optimization_task,
                sustainability_task
            ]
        )

        crew = Crew(
            agents=[
                solution_agent,
                operational_excellence_agent,
                security_agent, reliability_agent,
                performance_efficiency_agent,
                cost_optimization_agent,
                sustainability_agent,
                evaluation_agent
            ],
            tasks=[
                solution_task,
                operational_excellence_task,
                security_task, reliability_task,
                performance_efficiency_task,
                cost_optimization_task,
                sustainability_task,
                evaluate_task
            ],
            verbose=1,
            process=Process.sequential
        )
        result = crew.kickoff()
        print(f"START-----usage metrics----")
        print(crew.usage_metrics)
        print(f"-----usage metrics----END")
        return result
