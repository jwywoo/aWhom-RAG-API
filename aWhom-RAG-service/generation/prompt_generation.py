from template_enums.template_persnoa_enum import TemplatePersonaEnum
from langchain.prompts import ChatPromptTemplate


def get_prompt_generation(selected_prompt):
    persona_enum = TemplatePersonaEnum
    combined_persona = persona_enum.persona_role_template_front.value + selected_prompt + persona_enum.persona_context_template.value
    return ChatPromptTemplate.from_template(combined_persona)