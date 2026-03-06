"""Command-line interface for speciesfyi."""

from __future__ import annotations

import json

import typer

from speciesfyi.api import SpeciesFYI

app = typer.Typer(help="SpeciesFYI — Species taxonomy and biodiversity API client.")


@app.command()
def search(query: str) -> None:
    """Search speciesfyi.com."""
    with SpeciesFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
