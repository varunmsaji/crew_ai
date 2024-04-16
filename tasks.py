from textwrap import dedent
from crewai import Task

class Meeting_prep_tasks():
    def research_task(self, agent, participants, meeting_context):
        return Task(
            description=dedent(f"""\
            Conduct comprehensive research on each of the individuals and companies
            involved in the upcoming meeting. Gather information on recent
            news, achievements, professional background, and any relevant
            business activities.

            Participants: {participants}
            Meeting Context: {meeting_context}"""),
            expected_output=dedent("""\
            A detailed report summarizing key findings about each participant
            and company, highlighting information that could be relevant for the meeting."""),
            async_execution=True,
            agent=agent
        )
    
    def industry_analysis_task(self,agent,participants,meeting_context):
        return Task(
            description =dedent(f""" \
            Analyze the current industry trends,challenges,and oppertunities 
            relevant to the meeting's context.Consider market reports,recent
            developments,and expert opinions to provide a comprehensive
            overview of the industry lanscapr.
            Participants:{participants}
            meeting Context:{meeting_context}"""),
            expected_output = dedent("""\ 
            An insightful analaysis that identifies major trends ,potential
         challenges,and strategic oppertunities"""),
            async_execution=True,
            agent =agent
        )
    
    def meeting_strategy_task(self,agent,meeting_context,meeting_objective):
        return Task(
            description=dedent(f"""\
            Develop strategic talking points,questions, and discussion angles 
            for the meeting based on the research and industry analysis conducted
            Meeting Context:{meeting_context}
            Meeting Objective:{meeting_objective}"""),
                        expected_output=dedent(""" \
            Complete report with a list of key talking points,strategic questions
            to ask to help achieve the meetings objective during the meeting"""),
            agent = agent
        )
    
    def summary_and_briefing_task(self,agent,meeting_context,meeting_objective):
        return Task(
            description=dedent(f""" \
            Compile all the research findings,industry analysis,and strategic
            talking points into a concise,comprehensive briefing document for the meeting
            Ensure the breifing is easy to digest and equips the meeting participants
            wit all the necessary information and strategies 
            Meeting Context:{meeting_context}
            Meeting objective:{meeting_objective}"""),
            expected_output=dedent("""\
            A well-structures briefing document that includes sections for participants
            bios,industry overview,talking points,and strategic recommendations"""),
            agent=agent
                    )