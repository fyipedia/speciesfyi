"""MCP server for speciesfyi — AI assistant tools for speciesfyi.com.

Run: uvx --from "speciesfyi[mcp]" python -m speciesfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SpeciesFYI")


@mcp.tool()
def list_discoveries(limit: int = 20, offset: int = 0) -> str:
    """List discoveries from speciesfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from speciesfyi.api import SpeciesFYI

    with SpeciesFYI() as api:
        data = api.list_discoveries(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No discoveries found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_discovery(slug: str) -> str:
    """Get detailed information about a specific discovery.

    Args:
        slug: URL slug identifier for the discovery.
    """
    from speciesfyi.api import SpeciesFYI

    with SpeciesFYI() as api:
        data = api.get_discovery(slug)
        return str(data)


@mcp.tool()
def list_ecoregions(limit: int = 20, offset: int = 0) -> str:
    """List ecoregions from speciesfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from speciesfyi.api import SpeciesFYI

    with SpeciesFYI() as api:
        data = api.list_ecoregions(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No ecoregions found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_species(query: str) -> str:
    """Search speciesfyi.com for species, ecoregions, and biodiversity.

    Args:
        query: Search query string.
    """
    from speciesfyi.api import SpeciesFYI

    with SpeciesFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
