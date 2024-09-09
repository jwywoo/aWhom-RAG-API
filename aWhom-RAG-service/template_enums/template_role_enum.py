from enum import Enum

class TemplateRoleEnum(Enum):
    template_role_front = "You are an expert script writer and have information about the role that actor should play."

    template_role_rear = "Your role is making sure the actor get relevant information to act and answer the given task from the database"
    
    template_index_explanations = """
    Here are the explanation about the database
    Each row can be a question or an answer between the role and his or her friends
    Since your actor is playing the role of Woo make sure you focus the answer of Woo.
    Every row is in Korean while column names are in English.
    Provide these alternative questions separated by newlines.
    Original question: {question}"""