import typer

app = typer.Typer()

@app.command()
def generate():
    print("Generating report...")

@app.command()
def validate():
    print("Validating data...")

@app.command()
def templates():
    print("Available templates")

if __name__ == "__main__":
    app()
