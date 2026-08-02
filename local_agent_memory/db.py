import sqlite3
from datetime import datetime
from pathlib import Path


class AgentMemoryDB:
    def __init__(self, db_path: str = ".agent_memory.db"):
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()
        
    def _init_db(self):
        """Initialize the database with FTS5 for full-text search."""
        cursor = self.conn.cursor()
        
        # We use an FTS5 virtual table for extremely fast keyword search
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS memories USING fts5(
                content, 
                tags, 
                timestamp UNINDEXED
            )
        ''')
        self.conn.commit()
        
    def add_memory(self, content: str, tags: str = "") -> None:
        """Add a new memory to the database."""
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()  # noqa: DTZ005
        cursor.execute(
            "INSERT INTO memories (content, tags, timestamp) VALUES (?, ?, ?)",
            (content, tags, timestamp)
        )
        self.conn.commit()
        
    def search(self, query: str, limit: int = 5) -> list[dict]:
        """Search memories using FTS5 match query."""
        cursor = self.conn.cursor()
        
        # If query is empty, return latest
        if not query.strip():
            cursor.execute(
                "SELECT rowid, * FROM memories ORDER BY timestamp DESC LIMIT ?", 
                (limit,)
            )
        else:
            # Simple sanitization for FTS5 syntax
            safe_query = query.replace('"', '""')
            fts_query = f'"{safe_query}"*'
            
            try:
                cursor.execute(
                    "SELECT rowid, * FROM memories WHERE memories MATCH ? ORDER BY rank LIMIT ?",
                    (fts_query, limit)
                )
            except sqlite3.OperationalError:
                # Fallback to LIKE if FTS parsing fails due to special characters
                cursor.execute(
                    "SELECT rowid, * FROM memories WHERE content LIKE ? OR tags LIKE ? ORDER BY timestamp DESC LIMIT ?",
                    (f"%{query}%", f"%{query}%", limit)
                )
                
        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row["rowid"],
                "content": row["content"],
                "tags": row["tags"],
                "timestamp": row["timestamp"]
            })
            
        return results

    def delete_memory(self, memory_id: int) -> bool:
        """Delete a memory by its rowid."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM memories WHERE rowid = ?", (memory_id,))
        self.conn.commit()
        return cursor.rowcount > 0
        
    def clear_all(self) -> None:
        """Clear all memories."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM memories")
        self.conn.commit()
