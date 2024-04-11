from crewai.task import TaskOutput

def task_callback(output: TaskOutput, aspect: str, task_responses: dict):
    if task_responses is not None:
        task_responses[aspect] = output.raw_output
        print(f"-------------------{task_responses[aspect]}")
    else:
        print(f"-------------------empty")

def create_task_callback(aspect: str, task_responses: dict = None):
    def callback(output: TaskOutput):
        task_callback(output, aspect, task_responses)
    return callback