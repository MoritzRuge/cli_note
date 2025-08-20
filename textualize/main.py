from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Static

class Hello(Static):
    """Display a Greeting."""
    BORDER_TITLE = "Hello Widget"
    def on_mount(self) -> None:
        self.border_subtitle = "Test"
        self.update("Hello, [b]World[/b]!")

class CustomApp(App):
    CSS_PATH = "myapp.tcss"
    def compose(self) -> ComposeResult:
        yield Hello()

if __name__ == "__main__":
    app = CustomApp()
    app.run()
