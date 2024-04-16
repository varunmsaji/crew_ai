import os 
from exa_py import Exa
from langchain.agents import tool
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get('OPENAI_API_KEY'))

class Exa_search_tool_set():
    @tool
    def search(query:str):
        """"Search for a webpage based on the query """
        return Exa_search_tool_set._exa().search(f"{query}",use_autoprompt=True,num_results=3)
    
    @tool
    def find_similar(url:str):
        """"Search the webpages similar to a given URL.
        The url passed in shoiuld be a URL returned from 'search'."""
        return Exa_search_tool_set._exa().find_similar(url,num_results=3)
    
    @tool 
    def get_contents(ids:str):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list od ids returned from 'search'."""
        print("ids from param:",ids)
        ids = eval(ids)
        print("eval ids:",ids)
        contents = str(Exa_search_tool_set._exa().get_contents(ids))
        print(contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)
    
    def tools():
        return [
            Exa_search_tool_set.search,
            Exa_search_tool_set.find_similar,
            Exa_search_tool_set.get_contents
        ]


    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))



print(Exa_search_tool_set._exa())