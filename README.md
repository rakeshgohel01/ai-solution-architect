# AI Solution Architect
- [AI Solution Architect](#ai-solution-architect)
	- [Try It Out](#try-it-out)
	- [Introduction](#introduction)
		- [Prerequisites](#prerequisites)
		- [Installation](#installation)
		- [Model Selection](#model-selection)
		- [Run AI Solution Architect](#run-ai-solution-architect)
			- [Well-architected Pillar Rating](#well-architected-pillar-rating)
	- [CrewAI Framework](#crewai-framework)
	- [AI Agents at work](#ai-agents-at-work)
	- [Details \& Explanation](#details--explanation)
	- [Limitations](#limitations)
	- [Contributing](#contributing)
	- [Disclaimer](#disclaimer)
	- [License](#license)

## Try It Out

You can try out the [@AI Solution Architect](https://architect.juteq.ca) live. This demo lets you experience the functionality of the solution without any setup required.

## Introduction

The AI Solution Architect Agent leverages cutting-edge user selected AI models to offer cloud architecture recommendations based on the Well-Architected Framework. It aims to enhance operational excellence, security, reliability, performance efficiency, and cost optimization for cloud infrastructures across major providers (now AWS).

By [@rakeshgohel01](https://linkedin.com/in/rakeshgohel01)


### Prerequisites
- Python 3.10 or higher
- poetry for Python package installation
- Access to Serper, OpenAI and Anthropic APIs

### Installation
Clone the repository:
```bash
git clone https://github.com/rakeshgohel01/ai-solution-architect.git
cd ai-solution-architect
```

Install the required Python packages:
```bash
pipx install poetry
poetry install --no-root
```
Copy .env.example to .env and fill in your API keys for [Serper](https://serper.dev/), [OpenAI](https://platform.openai.com/api-keys) and [Anthropic](https://serper.dev/)

```bash
cp .env.example .env
```

### Model Selection

To configure the AI models, add the following lines to your .env.

```plaintext
# AI Model Configurations
OPENAI_MODEL_NAME=gpt-3.5-turbo
ANTHROPIC_MODEL_NAME=claude-3-haiku-20240307
```
*Using GPT-4 and Claude Opus models will cost you more money.*

### Run AI Solution Architect
```bash
python main.py
```

#### Well-architected Pillar Rating
It has default ratings set for a given well-architected pillar. User can request how far to adhere to a given pillar. 100% rating expect all aspects of well-architected pillar are satisfied in the proposed solution.

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to choose between different of aspects of solution and recommend based on ratings requested for each well-architected pillar.

## AI Agents at work
There are total 8 agents working together to recommend the best architecture
- Solution Architect: Expert architect in cloud computing and solution architecture on AWS
- Operation Excellence: Expert in Operational Excellence
- Security: Expert in Security Posture design
- Reliablity: Expert in archtecting system reliability
- Performance Efficiency: Expert in architecting performance efficiency of the system
- Cost Optimization: Expert in optimizing cost of the system
- Sustainablity: Expert in addressing environmental sustaianablity
- Evaluator: Evaluates cloud computing and solution architecture

## Details & Explanation
- **Running the Script**: Execute `python main.py`` and input your architectural problem when prompted. The script will leverage the CrewAI framework to process the problem and architect a solution.
- **Key Components**:
  - `./main.py`: Main script file for input.
  - `./architect.py`: AI agent orchestrator
  - `./agents/aws_agents.py`: All agents working together to produce result
  - `./tasks/aws_tasks.py`: Task assigned to individual agent
  - `./tools`: Contains tool classes used by the agents.

## Limitations
The quality and accuracy of the generated answers depend on the performance of the selected model and the relevance of the search results from SERPAPI.

The script may take a considerable amount of time to execute, especially for complex topics with multiple subtopics.

## Contributing

Contributions to the AI Solution Architect are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## Disclaimer

AI Solution Architect is an experimental tool and should be used for informational purposes only. The generated reports may contain inaccuracies or inconsistencies. Always verify the information obtained from the script with reliable sources before making any decisions based on it.

## License
This project is released under the MIT License.
