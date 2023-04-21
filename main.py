from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class Service:
    def __init__(self):
        self.openai = OpenAI
        self.promptTemplate = PromptTemplate
        self.lLMChain = LLMChain

    def send(self, message):
        LLM = self.openai(temperature=.7)

        answer_chain = self.lLMChain(llm=LLM, prompt=self.prompt_template())

        respond = answer_chain.run(message)
        return respond

    @staticmethod
    def template_text():
        return """
        Question: {text}
        Answer:
        """

    def prompt_template(self):
        return self.promptTemplate(input_variables=['text'], template=self.template_text())
