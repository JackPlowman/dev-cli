import typer
from git import Repo

app = typer.Typer()


@app.command()
def state(message: str) -> None:
    """Commit changes with state message.

    Args:
        message (str): The message to commit with.
    """
    repo = Repo(".")
    repo.index.commit(f"Add State for {message}")


if __name__ == "__main__":
    app()
