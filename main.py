#creating task which the main of the crew
from dotenv import load_dotenv
from crewai import Crew
from tasks import Meeting_prep_tasks
from agents import Meeting_prep_agents

def main():
    load_dotenv()
    print("welcome to the meeting prep crew")
    print('-'*50)
    meeting_participants = input("what are the emails for the participants (other than you) in the meeting\n")
    meeting_context = input("what is the context of the meeting\n")
    meeting_objective = input("what is your objective for the meeting\n")

    tasks = Meeting_prep_tasks()
    agents = Meeting_prep_agents()

    #initialize agents
    research_agent = agents.research_agent()
    industry_analysis_agent = agents.industry_analysis_agent()
    meeting_strategy_agent = agents.meeting_strategy_agent()
    summary_and_briefing_agent = agents.summary_and_briefing_agent()

    #create the tasks
    research_task = tasks.research_task(research_agent,meeting_participants,meeting_context)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent,meeting_participants,meeting_context)
    meeting_strategy_task = tasks.meeting_strategy_task(meeting_strategy_agent,meeting_context,meeting_objective)
    summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent,meeting_context,meeting_objective)

    meeting_strategy_task.context = [research_task,industry_analysis_task]
    summary_and_briefing_task.context = [research_task,industry_analysis_task,meeting_strategy_task]

    crew = Crew(
        agents=[
            research_agent,
            industry_analysis_agent,
            meeting_strategy_agent,
            summary_and_briefing_agent
        ],
        tasks = [
            research_task,
            industry_analysis_task,
            meeting_strategy_task,
            summary_and_briefing_task
        ]
        
    )
    results = crew.kickoff()
    print(results)















if __name__=="__main__":
    main()