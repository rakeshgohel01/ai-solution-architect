from crewai import Task
from textwrap import dedent
from datetime import date


class AWSTasks():
  def solution_task(self, agent, problem, weights, callback):
    print(f"solution callback {callback}")
    return Task(
      description=dedent(
        f"""
        **Task**: Design Technical Solution

        **Description**:
        You are tasked with designing a technical solution to address a specific business problem. Your objective is to suggest a realistic and implementable solution that is as simple as possible while effectively addressing the problem. The solution should be detailed, taking into consideration the current technological landscape and best practices in software architecture and cloud computing.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        Realism and Implementability: Your proposed solution must be feasible within the constraints of current technology, budget, and time. It should leverage existing tools and platforms where appropriate, avoiding over-engineering or excessively complex designs.
        Simplicity Over Complexity: While maintaining effectiveness, the solution should prioritize simplicity. Simple solutions are generally more robust, easier to maintain, and quicker to implement.
        Detailed Final Answer: Provide a comprehensive outline of the solution, including the architecture, technologies to be used, and a high-level implementation plan. If possible, include reasoning behind key architectural and technological choices to offer insight into your decision-making process.

        Evaluate pillar only above 50%

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        agent=agent,
        expected_output="""
        A comprehensive description of the proposed technical solution, addressing the business problem.An outline of the solution architecture, including diagrams if applicable. A list of the key components and technologies required for the implementation, ensuring there are no overlaps and that each component serves a specific purpose within the solution. Justification for critical architectural and technological choices, highlighting how they contribute to addressing the business problem effectively. Considerations for future scalability, maintenance, and potential integration with existing systems or workflows.
        """,
        # output_file="solution.txt",
        callback=callback,
      )

  def evaluate_task(self,
                    agent,
                    problem,
                    weights,
                    callback,
                    contextTasks=None
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluate Solution Architecture

        **Description**:
          You are tasked with conducting a thorough evaluation of a proposed technical solution. This evaluation should focus on the solution's alignment with key architectural pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

          You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

          Assessment Criteria: Each pillar represents a fundamental aspect of a well-architected solution. You will assess the proposed solution against these pillars, considering the current implementation and potential for improvement.
          User Weights: The importance of each pillar is quantified by user-defined weights on a scale of 0 to 1, with 1 being the most important. These weights reflect the business or project-specific priorities and should guide the emphasis of your evaluation.
          Scoring System: Initially, assume a perfect score (5) for each pillar to calculate a baseline total score. This represents the ideal state where the solution excels in all areas. Then, using the actual ratings provided for the solution's performance in each pillar, calculate the new total score. This approach allows for a comparative analysis of the solution's current state against the ideal.

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        context=contextTasks,
        async_execution=False,
        agent=agent,
        expected_output="""
        Detailed Evaluation: Provide an in-depth analysis of the proposed solution, assessing its strengths and weaknesses across the operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability pillars.
        Base Total Score: Calculate and display the base total score by multiplying the perfect score (5) by the weight of each pillar and summing these values. This score reflects the maximum possible score the solution could achieve if it were ideal across all pillars.
        New Total Score: Calculate and display the new total score by multiplying the actual rating received for each pillar by its corresponding weight and summing these values. This score provides a realistic assessment of the solution's alignment with the well-architected framework, taking into account the specified priorities.

        Instructions for Comprehensive Analysis:

        Justify the ratings provided for each pillar based on the information available about the proposed solution. Highlight specific features or aspects of the solution that contribute to its rating in each area. Discuss any discrepancies between the base total and new total scores, offering insights into how the solution could be improved to better meet the criteria set forth by the architectural pillars. Suggest actionable recommendations for enhancing the solution's architecture, considering the feasibility of such improvements and their potential impact on meeting the project's objectives.
        """,
        # output_file="final.txt",
        callback=callback
      )

  def operational_excellence_task(self,
                    agent,
                    problem,
                    weights,
                    contextTasks,
                    callback
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluation Solution for Operational Excellence

        **Description**:
        You are assigned to evaluate the alignment of a proposed technical solution with key principles of operational excellence. These principles are essential for maintaining a resilient, efficient, and adaptable operation. Your evaluation should focus on the following operational excellence principles:

        1. Perform Operations as Code: Assess the degree to which the solution automates operations, making them repeatable and less prone to human error.
        2. Make Frequent, Small, Reversible Changes: Determine the solution's ability to implement changes in a controlled, reversible manner, allowing for quick adaptation and rollback if necessary.
        3. Refine Operations Procedures Frequently: Evaluate the solution's approach to continuous improvement in operational practices.
        4. Anticipate Failures: Examine how the solution predicts and prepares for potential failures, enhancing reliability.
        5. Learn from All Operational Failures: Assess the mechanisms in place for learning from failures and incorporating lessons into future operations.
        6. Use Managed Services: Evaluate the extent to which the solution leverages managed services to reduce operational overhead and complexity.
        7. Implement Observability for Actionable Insights: Determine how the solution implements observability (monitoring, logging, alerting) to provide insights into its performance and health.
        For each principle, provide a rating on a scale of 1 to 5, with 5 being excellent and 1 indicating that the solution has significant room for improvement in that area.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        context=contextTasks,
        agent=agent,
        expected_output=f"""
        Begin with a thorough analysis of the proposed solution, detailing its adherence to each of the operational excellence principles listed above. Highlight specific practices, tools, or methodologies employed by the solution that contribute to its rating in each principle.
        Ratings:
        Perform Operations as Code: [Rating]
        Make Frequent, Small, Reversible Changes: [Rating]
        Refine Operations Procedures Frequently: [Rating]
        Anticipate Failures: [Rating]
        Learn from All Operational Failures: [Rating]
        Use Managed Services: [Rating]
        Implement Observability for Actionable Insights: [Rating]

        Provide a final section summarizing the overall alignment of the solution with operational excellence principles. Discuss areas of strength and opportunities for improvement, offering actionable recommendations that could enhance the solution's operational effectiveness.
        """,
        # output_file="operational_excellence.txt",
        callback=callback
      )

  def security_task(self,
                    agent,
                    problem,
                    weights,
                    contextTasks,
                    callback
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluate solution for security compliance

        **Description**:
        You are assigned to evaluate the security posture of a proposed technical solution, focusing on its alignment with established security principles and cloud security domains. This evaluation encompasses a broad range of security aspects, from identity and access management (IAM) to data protection and incident response. Your objective is to assess how well the solution adheres to the following security principles:

        Implement a Strong Identity Foundation: Evaluate the solution's approach to managing identities and access control, ensuring that principles of least privilege are applied.
        1. Maintain Traceability: Assess the solution's capabilities for logging and monitoring operations, ensuring accountability and traceability.
        2. Apply Security at All Layers: Determine whether the solution implements security measures across all layers, including network, application, and data layers.
        3. Automate Security Best Practices: Evaluate the extent to which the solution uses automation to enforce security controls and compliance.
        4. Protect Data in Transit and at Rest: Assess how the solution protects sensitive data both during transmission and while stored.
        5. Keep People Away from Data: Evaluate the measures in place to minimize direct access to sensitive data, reducing the risk of data breaches.
        6.Prepare for Security Events: Assess the solution's readiness for security incidents, including detection capabilities and response plans.

        Additionally, consider the solution's alignment with critical cloud security domains:

        Security Foundation
        IAM
        Detection
        Infrastructure Protection
        Data Protection
        Incident Response
        Application Security
        For each principle and domain, provide a rating on a scale of 1 to 5, where 5 indicates excellent adherence and 1 suggests significant areas for improvement.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        context=contextTasks,
        agent=agent,
        expected_output=f""""
        Detailed Evaluation: Provide an in-depth analysis of the proposed solution, detailing its adherence to each security principle and domain listed above. Highlight specific security practices, configurations, or tools employed by the solution that contribute to its rating in each area.
        Ratings:
        For each security principle and domain, provide a rating and justify the rating with specific observations or examples from the proposed solution. If assumptions are necessary, clearly state these and explain how they influenced your rating.
        Overall Security Posture: Summarize the solution's overall security posture, identifying strengths and highlighting areas where security practices could be improved. Offer actionable recommendations to enhance the solution's security compliance.
        """,
        # output_file="security.txt",
        callback=callback
      )

  def reliability_task(self,
                    agent,
                    problem,
                    weights,
                    contextTasks,
                    callback
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluate Solution Reliablity

        **Description**:
        You are assigned the role of assessing the reliability of a proposed technical solution, focusing on its robustness and resilience across key areas of reliability. This task involves a detailed evaluation based on the following reliability principles:

        1. Foundation: Assess whether the service quotas and network topology are adequately designed to accommodate the workload. This includes evaluating if the infrastructure setup can support the expected load and if it's configured for optimal performance and stability.
        2. Workload Architecture: Evaluate the architecture's design concerning its ability to prevent and mitigate failures. This involves assessing the system's redundancy, fault tolerance, and whether it incorporates design patterns that enhance reliability.
        3. Change Management: Determine the solution's capability to handle demanding changes without service disruption. This includes looking at deployment practices, the ability to roll back changes safely, and how changes are tested and validated before being applied to production environments.
        4. Failure Management: Assess the system's ability to detect failures promptly and automatically heal without significant intervention. This principle evaluates the monitoring, alerting, and automated recovery mechanisms in place.

        For each of these reliability principles, provide a rating on a scale of 1 to 5, with 5 representing excellent reliability and 1 indicating significant improvement needed.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        context=contextTasks,
        agent=agent,
        expected_output=f"""
        Offer a comprehensive analysis of the proposed solution against each of the four reliability principles. Highlight the specific aspects of the solution that contribute to its rating in each area, including architectural decisions, operational practices, and implemented technologies.
        Ratings:
        Foundation: [Rating]
        Workload Architecture: [Rating]
        Change Management: [Rating]
        Failure Management: [Rating]

        Summarize the solution's overall reliability posture based on these ratings. Identify the solution's strengths in maintaining high availability and resilience and point out areas where reliability could be enhanced. Provide actionable insights and recommendations for improving the solution's reliability, focusing on areas that scored lower in the evaluation.
        """,
        # output_file="reliability.txt",
        callback=callback
      )

  def performance_efficiency_task(self,
                    agent,
                    problem,
                    weights,
                    contextTasks,
                    callback
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluate Solution Performance Efficiency

        **Description**:
        This task involves a critical assessment of the proposed solution's ability to use computing resources efficiently, ensuring it meets the current requirements while remaining adaptable to changing demands and technological advancements. Your evaluation should focus on the following performance efficiency principles:

        1. Democratize Advanced Technologies: Assess how the solution leverages technology-as-a-service offerings to simplify access to cutting-edge technologies and reduce the need for in-house expertise.
        2. Go Global in Minutes: Evaluate the solution's capacity for deploying services in multiple regions to reduce latency and improve user experience globally.
        3. Use Serverless Architecture: Determine the extent to which the solution adopts serverless computing to minimize the operational burden associated with managing physical servers and scaling resources.
        4. Experiment More Often: Assess the solution's approach to utilizing automation for testing and experimentation, facilitating rapid iteration and innovation.
        5. Consider Mechanical Sympathy: Evaluate how well the solution's data access patterns and storage choices are aligned with the underlying hardware capabilities, optimizing for performance.

        For each principle, provide a rating on a scale of 1 to 5, where 5 signifies excellent performance efficiency and 1 indicates significant room for improvement.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        context=contextTasks,
        agent=agent,
        expected_output=f"""
        Provide an in-depth analysis of the proposed solution against each of the performance efficiency principles. Highlight specific practices, configurations, or technologies employed by the solution that contribute to its rating in each area.
        Ratings:
        Democratize Advanced Technologies: [Rating]
        Go Global in Minutes: [Rating]
        Use Serverless Architecture: [Rating]
        Experiment More Often: [Rating]
        Consider Mechanical Sympathy: [Rating]

        Conclude with a summary of the solution's overall performance efficiency based on these ratings. Identify areas where the solution excels in utilizing computing resources effectively and point out opportunities for enhancing performance efficiency. Offer actionable recommendations for improvement, particularly in areas that received lower ratings.
        """,
        # output_file="performance_efficiency.txt",
        callback=callback
      )

  def cost_optimization_task(self,
                    agent,
                    problem,
                    weights,
                    contextTasks,
                    callback
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluate Solution for Cost Optimization

        **Description**:
        This task involves evaluating the proposed solution's effectiveness in optimizing costs without compromising on functionality and performance. Your evaluation should focus on the solution's alignment with the following cost optimization principles:

        1. Implement Cloud Financial Management: Assess how well the solution integrates cloud financial management practices, ensuring that there is a dedicated effort to managing cloud costs and maximizing the value of cloud investments.
        2. Adopt a Consumption Model: Evaluate the extent to which the solution utilizes a consumption-based pricing model, paying only for the resources used and efficiently scaling up or down based on demand.
        3. Measure Overall Efficiency: Determine how the solution measures the efficiency of resource utilization against the business output, aiming to maximize output while minimizing costs.
        4. Stop Spending Money on Undifferentiated Heavy Lifting: Assess how the solution minimizes spending on non-core operations by leveraging managed services for data center operations, operating systems, and application management.
        5. Analyze and Attribute Expenditure: Evaluate the solution's approach to attributing IT costs to revenue streams and individual workload owners transparently, facilitating clear cost management and accountability.

        For each principle, provide a rating on a scale of 1 to 5, where 5 indicates excellent cost optimization and 1 suggests substantial improvement is needed.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        context=contextTasks,
        agent=agent,
        expected_output=f"""
        Offer an in-depth analysis of how the proposed solution adheres to each of the cost optimization principles. Highlight specific methodologies, technologies, or practices implemented within the solution that contribute to its rating in each area.
        Ratings:
        Implement Cloud Financial Management: [Rating]
        Adopt a Consumption Model: [Rating]
        Measure Overall Efficiency: [Rating]
        Stop Spending Money on Undifferentiated Heavy Lifting: [Rating]
        Analyze and Attribute Expenditure: [Rating]

        Conclude with a summary of the solution's overall approach to cost optimization. Identify strengths in managing and reducing costs effectively and pinpoint areas where cost optimization practices could be improved. Provide actionable recommendations for enhancing the solution's cost-efficiency, particularly focusing on areas that received lower ratings.
        """,
        # output_file="cost_optimization.txt",
        callback=callback
      )

  def sustainability_task(self,
                    agent,
                    problem,
                    weights,
                    contextTasks,
                    callback
                    ):
    return Task(
      description=dedent(
        f"""
        **Task**: Evaluate solution for Envrionment Sustainability

        **Description**:
        This task focuses on evaluating the proposed technical solution's commitment to environmental sustainability within the cloud computing ecosystem. Your analysis should concentrate on the solution's alignment with the following sustainability principles:

        1. Understand Your Impact: Assess how well the solution identifies and addresses its environmental impact, including the total energy consumption of cloud workloads and their carbon footprint.
        2. Establish Sustainability Goals: Evaluate the solution's goals related to sustainability, such as reducing the compute and storage resources required per transaction and minimizing energy usage.
        3. Maximize Utilization: Determine the efficiency of resource utilization within the solution, focusing on workload right-sizing to avoid over-provisioning and underutilization.
        4. Anticipate and Adopt New, More Efficient Hardware and Software Offerings: Assess how the solution stays informed about and integrates more efficient technologies to reduce environmental impact.
        5. Use Managed Services: Evaluate the extent to which the solution leverages cloud managed services to improve efficiency and reduce the operational overhead and energy consumption associated with maintaining physical infrastructure.
        6.Reduce the Downstream Impact of Cloud Workloads: Analyze efforts made by the solution to decrease the energy and resource demands of its operations, contributing to a smaller overall environmental footprint.

        For each of these sustainability principles, provide a rating on a scale of 1 to 5, where 5 indicates exemplary sustainability practices and 1 suggests significant areas for improvement.

        You are instructed to delve deeper into the analysis of any pillar rated above 70% importance

        **Parameters**:
        - Business Problem: {problem}
        - User Weights : {weights}

        **Note**: {self.__tip_section()}
      """),
        async_execution=False,
        context=contextTasks,
        agent=agent,
        expected_output=f"""
        Provide a comprehensive review of the proposed solution's approach to sustainability. Highlight how the solution's design and operational practices contribute to its ratings in each of the listed sustainability principles.
        Ratings:
        Understand Your Impact: [Rating]
        Establish Sustainability Goals: [Rating]
        Maximize Utilization: [Rating]
        Anticipate and Adopt New, More Efficient Hardware and Software Offerings: [Rating]
        Use Managed Services: [Rating]
        Reduce the Downstream Impact of Cloud Workloads: [Rating]

        Conclude with an overall assessment of the solution's sustainability posture. Identify areas where the solution excels in promoting environmental sustainability and highlight opportunities for further enhancements. Offer actionable recommendations for improving the solution's sustainability profile, especially focusing on areas that received lower ratings.
        """,
        # output_file="sustainability.txt",
        callback=callback
      )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"
