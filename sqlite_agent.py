from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools
from sqlalchemy import create_engine
import os
import dotenv

dotenv.load_dotenv()

engine = create_engine('sqlite:///./Chinook_Sqlite.sqlite')

agent = Agent(
    name='chinook SQLite agent',
    model=OpenAIChat(id='gpt-4o'),
    markdown=True,
    show_tool_calls=True,
    system_message='You are equipped with tools to manage my SQLite database.',
    tools=[SQLTools(db_engine=engine)],
    add_history_to_messages=True,
    retries=3,
    debug_mode=True
)

# Write request to print response in the ('')
agent.print_response('What is the total invoice collected in 2009?', stream=True)