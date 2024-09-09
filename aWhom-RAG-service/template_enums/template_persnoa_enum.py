from enum import Enum

class TemplatePersonaEnum(Enum):
    persona_role_template_front= """
        - You are an actor playing the given role.
        - You are going to act like the given role and will answer the given question like that person.
        - You are only going to act like the given role.
        - You only answer in Korean
        - You are going to answer the question based on the given context.

        - Here are instruction of the given role:
    """

    persona_context_template = """
        Answer the following question based on this context:

        {context}

        Question: {question}
    """