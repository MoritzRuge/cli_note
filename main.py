import click

def main():
    @click.command()
    def hello():
        click.echo("Hello from cli-note!")
    hello()


if __name__ == "__main__":
    main()
