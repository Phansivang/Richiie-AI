from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

chat_history = []


class Service:
    def __init__(self):
        self.openai = OpenAI
        self.promptTemplate = PromptTemplate
        self.lLMChain = LLMChain
        self.chat_history = []

    def send(self, message):
        chat_history.append(message)

        LLM = self.openai(temperature=.7)

        answer_chain = self.lLMChain(llm=LLM, prompt=self.prompt_template())

        respond = answer_chain.run(f'{message}')
        return respond

    @staticmethod
    def template_text():
        template = """%s Question: {text} Answer:""" % chat_history

        return template

    def prompt_template(self):
        return self.promptTemplate(input_variables=['text'], template=self.template_text())
