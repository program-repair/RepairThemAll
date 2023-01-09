
from core.database.engine import save
from core.database.schema import Result
from core.database.engine import get_engine
from core.database.schema import Base


def save_result():
    result = Result()
    result.benchmark = 'Defects4J'
    result.project = 'Chart'
    result.bug_id = 1
    result.request_type = 'SINGLE_FUNCTION'
    result.model = 'Codex'
    result.buggy_code_chunk = 'public void test() {'
    result.buggy_code_token = 10
    result.fixed_code_chunk = 'public void test() {'
    result.fixed_code_token = 10
    save(result)


def create_tables():
    Base.metadata.create_all(get_engine())


if __name__ == '__main__':
    create_tables()
    # save_result()
