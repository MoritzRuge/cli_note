import click
from main import list_all_notes, create_new_note, open_note

@click.version_option("0.1.0", prog_name="cli-note")
@click.group()
def cli():
    "Note taking CLI"
    pass

@cli.command()
@click.argument("title")
@click.argument("text")
def new(title, text):
    create_new_note(title, text)
    click.echo(f"Notiz '{title}' wurde erstellt!")

@cli.command()
@click.argument("title")
def open(title):
    open_note(title)

@cli.command()
def list():
    # List all Notes
    list_all_notes()

if __name__ == "__main__":
    cli()