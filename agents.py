from textwrap import dedent
from crewai import Agent
from tools import Exa_search_tool_set

class Meeting_prep_agents():
    def research_agent(self):
        return Agent(
            role = "research specialist",
            goal ='conduct thorough research on people and companies involved in the meeting',
            tools =Exa_search_tool_set.tools,
            backstory = dedent("""\
            As a research specialist,your mission is to uncover detailed information
            about the individual and entities participating in the meeting .Yor insights
            will lay the groundwork for strategic meeting preparations"""),
                        verbose = True
        )
    
    def industry_analysis_agent(self):
        return Agent(
            role = 'Industry Analysis',
            goal = 'Analysis the current industry trends,challenges and oppertunities',
            tools = Exa_search_tool_set.tools,
            backstory = dedent("""\
            As an industry Analyst ,your analysis will identify key trends
            challenges facing  the industry, and potential oppertunities that 
            could be leveraged during the meeting for strategic advantage"""),
            verbose = True
        )
    def meeting_strategy_agent(self):
        return Agent(
            role ='Meeting strategy advisor',
            goal = 'Develop talking points,question , and strategif angles for the meeting',
            backstory= dedent("""\
            As a strategic Advisor,your expertise will guide the development of
            talking points,insightful questions,and strategic angles
            to ensure the meeting's objectives are achieved"""),
            verbose =True
        )
    def summary_and_briefing_agent(self):
        return Agent(
            role = 'Breifing coordinator',
            goal = 'Compile all gathered information into concise,informative briefing document',
            bakstory = dedent("""\
            As the briefing coordinator,your role is to consolidate the research,
            analysis ,and strategic insights"""),
            verbose = True
        )