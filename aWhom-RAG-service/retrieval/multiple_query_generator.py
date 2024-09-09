from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from template_enums.template_role_enum import TemplateRoleEnum

def multiple_query_generation(selected_persona):
    template_role_front = TemplateRoleEnum.template_role_front
    template_role_rear = TemplateRoleEnum.template_role_rear
    template_index_exp = TemplateRoleEnum.template_index_explanations
    prompt_perspectives = ChatPromptTemplate.from_template(template_role_front.value + selected_persona +template_role_rear.value+ template_index_exp.value)
    return (
        prompt_perspectives
        | ChatOpenAI(temperature=0)
        | StrOutputParser()
        | (lambda x: x.split("\n"))
    )