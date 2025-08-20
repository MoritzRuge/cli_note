from textual.app import App, ComposeResult
from textual.widgets import Footer, DataTable

HEADER = [
    ("ToDo", "Notizen", "Git"),
]

class TabsApp(App):
    # bindings for the Footer Objkect
    BINDINGS = [
        ("a", "add", "Add tab"),
        ("r", "remove", "Remove active Tab"),
        ("c", "clear", "Clear tabs"),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        """Focus the tabs when the app starts."""
        table = self.query_one(DataTable)
        table.add_columns(*HEADER[0])
        #table.add_row()


        

if __name__ == "__main__":
    app = TabsApp()
    app.run()