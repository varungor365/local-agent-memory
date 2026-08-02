import pytest
import os
from local_agent_memory.db import AgentMemoryDB

@pytest.fixture
def memory_db(tmp_path):
    db_file = tmp_path / "test.db"
    db = AgentMemoryDB(str(db_file))
    yield db
    if db_file.exists():
        os.remove(db_file)

def test_add_and_search_memory(memory_db):
    memory_db.add_memory("The API key is stored in AWS Secrets Manager", "aws,secrets")
    memory_db.add_memory("We use PostgreSQL for the main database", "db")
    
    # Search specific
    results = memory_db.search("PostgreSQL")
    assert len(results) == 1
    assert "PostgreSQL" in results[0]["content"]
    
    # Search all
    results_all = memory_db.search("")
    assert len(results_all) == 2

def test_delete_memory(memory_db):
    memory_db.add_memory("Test memory")
    results = memory_db.search("")
    assert len(results) == 1
    
    mem_id = results[0]["id"]
    assert memory_db.delete_memory(mem_id) == True
    
    assert len(memory_db.search("")) == 0

def test_clear_all(memory_db):
    memory_db.add_memory("1")
    memory_db.add_memory("2")
    memory_db.clear_all()
    assert len(memory_db.search("")) == 0
