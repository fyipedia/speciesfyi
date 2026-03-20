"""HTTP API client for speciesfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install speciesfyi[api]``

Usage::

    from speciesfyi.api import SpeciesFYI

    with SpeciesFYI() as api:
        items = api.list_countries()
        detail = api.get_country("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class SpeciesFYI:
    """API client for the speciesfyi.com REST API.

    Provides typed access to all speciesfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://speciesfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://speciesfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_discoveries(self, **params: Any) -> dict[str, Any]:
        """List all discoveries."""
        return self._get("/api/v1/discoveries/", **params)

    def get_discovery(self, slug: str) -> dict[str, Any]:
        """Get discovery by slug."""
        return self._get(f"/api/v1/discoveries/" + slug + "/")

    def list_ecoregions(self, **params: Any) -> dict[str, Any]:
        """List all ecoregions."""
        return self._get("/api/v1/ecoregions/", **params)

    def get_ecoregion(self, slug: str) -> dict[str, Any]:
        """Get ecoregion by slug."""
        return self._get(f"/api/v1/ecoregions/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_field_guides(self, **params: Any) -> dict[str, Any]:
        """List all field guides."""
        return self._get("/api/v1/field-guides/", **params)

    def get_field_guide(self, slug: str) -> dict[str, Any]:
        """Get field guide by slug."""
        return self._get(f"/api/v1/field-guides/" + slug + "/")

    def list_food_webs(self, **params: Any) -> dict[str, Any]:
        """List all food webs."""
        return self._get("/api/v1/food-webs/", **params)

    def get_food_web(self, slug: str) -> dict[str, Any]:
        """Get food web by slug."""
        return self._get(f"/api/v1/food-webs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_guide_series(self, **params: Any) -> dict[str, Any]:
        """List all guide series."""
        return self._get("/api/v1/guide-series/", **params)

    def get_guide_sery(self, slug: str) -> dict[str, Any]:
        """Get guide sery by slug."""
        return self._get(f"/api/v1/guide-series/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_habitats(self, **params: Any) -> dict[str, Any]:
        """List all habitats."""
        return self._get("/api/v1/habitats/", **params)

    def get_habitat(self, slug: str) -> dict[str, Any]:
        """Get habitat by slug."""
        return self._get(f"/api/v1/habitats/" + slug + "/")

    def list_ranks(self, **params: Any) -> dict[str, Any]:
        """List all ranks."""
        return self._get("/api/v1/ranks/", **params)

    def get_rank(self, slug: str) -> dict[str, Any]:
        """Get rank by slug."""
        return self._get(f"/api/v1/ranks/" + slug + "/")

    def list_species(self, **params: Any) -> dict[str, Any]:
        """List all species."""
        return self._get("/api/v1/species/", **params)

    def get_specy(self, slug: str) -> dict[str, Any]:
        """Get specy by slug."""
        return self._get(f"/api/v1/species/" + slug + "/")

    def list_taxa(self, **params: Any) -> dict[str, Any]:
        """List all taxa."""
        return self._get("/api/v1/taxa/", **params)

    def get_taxa(self, slug: str) -> dict[str, Any]:
        """Get taxa by slug."""
        return self._get(f"/api/v1/taxa/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> SpeciesFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
