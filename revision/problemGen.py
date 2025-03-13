from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import JsonOutputParser
import json
from pydantic import BaseModel, Field
from langchain_ollama.llms import OllamaLLM
from langchain_groq import ChatGroq

class Problem(BaseModel):
    title: str = Field(description="title of the problem")
    description: str = Field(description="short description of the problem")
    link: str = Field(description="link for the problem")
    frequency: int = Field(description="frequency of the problem")


# And a query intented to prompt a language model to populate the data structure.


def GenerateProblems(problem_query):
        model = ChatGoogleGenerativeAI(
                    model="gemini-1.5-pro",
                    temperature=0,
                    max_tokens=None,
                    timeout=None,
                    max_retries=2,
                    # other params...
                )
        # model = ChatGroq(model="qwen-2.5-32b",
        #                 temperature=0.6,
        #                 )
        # model = OllamaLLM(model="deepseek-r1")

        # Set up a parser + inject instructions into the prompt template.
        parser = JsonOutputParser(pydantic_object=Problem)

        prompt = PromptTemplate(
            template="As an interviewer of certain startup or MNC suggest.\n{format_instructions}\n{query}\n",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )


        chain = prompt | model | parser
        return chain.invoke({"query": problem_query})