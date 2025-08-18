import click

def main():
    @click.command()
    @click.version_option("0.1.0", prog_name="cli-note")
    def hello():
        click.echo("Hello from cli-note!")
    hello()


if __name__ == "__main__":
    main()
