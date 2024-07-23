from app.recognizer.brackets.braces import BRACES_MAPPER
from app.recognizer.brackets.parentheses import PARENTHESES_MAPPER

BRACKETS_MAPPER = dict()
BRACKETS_MAPPER.update(PARENTHESES_MAPPER)
BRACKETS_MAPPER.update(BRACES_MAPPER)