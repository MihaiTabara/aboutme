from click import CommandCollection
from app.app import create_app
from app.manager import cli as manager_cli

app = create_app()

if __name__ == "__main__":
    cli = CommandCollection(sources=[manager_cli])
    cli(obj={'app':app})
