from sqlalchemy import JSON, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

from core.database.engine import get_engine

Base = declarative_base()


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    model = Column(String(100), nullable=False)
    benchmark = Column(String(100), nullable=False)
    project = Column(String(100), nullable=False)
    bug_id = Column(Integer(), nullable=False)
    request_type = Column(String(100))  # single line, function, single hunk
    prompt_text = Column(Text)
    prompt_size = Column(Integer())
    patch = Column(Text)
    buggy_code_chunk = Column(Text)
    buggy_code_token = Column(Integer())
    fixed_code_chunk = Column(Text)
    fixed_code_token = Column(Text)
    respond_code_chunk = Column(Text)
    respond_code_size = Column(Integer())
    respond_compiled_output = Column(Text)
    created_on = Column(DateTime(), default=datetime.now)
    # for example, turn on/off comments or document
    prompt_params = Column(JSON)
    # for example, codex params
    request_params = Column(JSON)
    # CODE_TOO_LONG, ERROR, SYNTAX_INCORRECT, SYNTAX_CORRECT, SEMANTIC_CORRECT
    result_type = Column(String(100))
    # record error message if result_type is ERROR
    error_message = Column(Text)


def run():
    Base.metadata.create_all(get_engine())
