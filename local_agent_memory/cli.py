import argparse
import sys

from rich.console import Console
from rich.table import Table

from . import __version__
from .db import AgentMemoryDB

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🧠 Local Agent Memory Hub")
    parser.add_argument("--version", action="version", version=f"local-agent-memory {__version__}")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new memory")
    add_parser.add_argument("content", help="The content to remember")
    add_parser.add_argument("--tags", "-t", default="", help="Comma separated tags")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search memories")
    search_parser.add_argument("query", nargs="?", default="", help="Search query")
    search_parser.add_argument("--limit", "-l", type=int, default=5, help="Max results to return")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a memory")
    delete_parser.add_argument("id", type=int, help="ID of the memory to delete")
    
    # Clear command
    subparsers.add_parser("clear", help="Clear all memories")

    args = parser.parse_args()
    
    try:
        db = AgentMemoryDB()
    except Exception as e:  # noqa: BLE001
        console.print(f"[red]Failed to initialize database: {e}[/red]")
        sys.exit(1)
        
    if args.command == "add":
        db.add_memory(args.content, args.tags)
        console.print("[green]✅ Memory saved.[/green]")
        
    elif args.command == "search":
        results = db.search(args.query, args.limit)
        if not results:
            console.print("[yellow]No memories found.[/yellow]")
            return
            
        table = Table(title=f"Memories matching '{args.query}'" if args.query else "Recent Memories")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Content", style="white")
        table.add_column("Tags", style="green")
        
        for row in results:
            table.add_row(str(row["id"]), row["content"], row["tags"])
            
        console.print(table)
        
    elif args.command == "delete":
        if db.delete_memory(args.id):
            console.print(f"[green]✅ Deleted memory {args.id}.[/green]")
        else:
            console.print(f"[red]❌ Memory {args.id} not found.[/red]")
            
    elif args.command == "clear":
        db.clear_all()
        console.print("[green]✅ All memories cleared.[/green]")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
