"""MCP server for speciesfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from speciesfyi.api import SpeciesFYI

mcp = FastMCP("speciesfyi")


@mcp.tool()
def search_speciesfyi(query: str) -> dict[str, Any]:
    """Search speciesfyi.com for content matching the query."""
    with SpeciesFYI() as api:
        return api.search(query)
