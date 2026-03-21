# speciesfyi

[![PyPI version](https://agentgif.com/badge/pypi/speciesfyi/version.svg)](https://pypi.org/project/speciesfyi/)
[![Python](https://img.shields.io/pypi/pyversions/speciesfyi)](https://pypi.org/project/speciesfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/speciesfyi/)

Python API client for the world's species taxonomy and biodiversity data. Access 49,112 species records, 17,982 taxa across the full Linnaean hierarchy, 846 ecoregions mapped to WWF biomes, and habitat classification data — all through a clean REST API with zero core dependencies.

Extracted from [SpeciesFYI](https://speciesfyi.com/), a species taxonomy reference platform cataloging biodiversity across all kingdoms of life with taxonomic classification, IUCN conservation status, geographic distribution, and ecological data used by researchers, educators, and conservation professionals.

> **Explore species data at [speciesfyi.com](https://speciesfyi.com/)** — browse [species](https://speciesfyi.com/species/), [taxa](https://speciesfyi.com/taxa/), [ecoregions](https://speciesfyi.com/ecoregions/), [habitats](https://speciesfyi.com/habitats/), and [field guides](https://speciesfyi.com/field-guides/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/speciesfyi/main/demo.gif" alt="speciesfyi demo — species taxonomy lookup, ecoregion data, and biodiversity search in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Taxonomic Classification](#taxonomic-classification)
  - [IUCN Conservation Status](#iucn-conservation-status)
  - [Ecoregions and Biomes](#ecoregions-and-biomes)
  - [Habitats and Ecosystems](#habitats-and-ecosystems)
  - [Food Webs and Ecology](#food-webs-and-ecology)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Species](#learn-more-about-species)
- [Nature FYI Family](#nature-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install speciesfyi                # Core (zero deps)
pip install "speciesfyi[cli]"         # + Command-line interface (typer, rich)
pip install "speciesfyi[mcp]"         # + MCP server for AI assistants
pip install "speciesfyi[api]"         # + HTTP client for speciesfyi.com API
pip install "speciesfyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from speciesfyi speciesfyi search "bald eagle"
```

## Quick Start

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    # Search across all species, taxa, and ecoregions
    results = api.search("gray wolf")
    print(results)

    # Get detailed species information
    species = api.get_specy("gray-wolf")
    print(species["name"])  # Gray Wolf

    # Browse taxonomic ranks
    taxa = api.list_taxa()
    print(taxa["count"])  # 17,982 taxa records

    # Explore ecoregions mapped to WWF biomes
    ecoregions = api.list_ecoregions()
    print(ecoregions["count"])  # 846 ecoregions
```

## What You Can Do

### Taxonomic Classification

All life on Earth is organized through the **Linnaean taxonomic hierarchy**, a system developed by Carl Linnaeus in 1735 and refined over nearly three centuries. SpeciesFYI catalogs 17,982 taxa across all 8 major ranks, from the broadest domains down to individual species.

| Rank | Description | Example |
|------|-------------|---------|
| **Domain** | Highest level of classification | Eukarya |
| **Kingdom** | Major groups of organisms | Animalia, Plantae, Fungi |
| **Phylum** | Body plan organization | Chordata (vertebrates), Arthropoda |
| **Class** | Shared physiological traits | Mammalia, Aves, Reptilia |
| **Order** | Groupings within classes | Carnivora, Primates, Passeriformes |
| **Family** | Closely related genera | Canidae (dogs), Felidae (cats) |
| **Genus** | Group of closely related species | *Canis*, *Panthera*, *Aquila* |
| **Species** | Fundamental unit of classification | *Canis lupus*, *Panthera leo* |

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    # Browse all taxonomic ranks in the hierarchy
    ranks = api.list_ranks()
    print(ranks["count"])  # 8 major ranks

    # Get all taxa — families, orders, classes, and more
    taxa = api.list_taxa()
    for taxon in taxa["results"][:3]:
        print(f"{taxon['rank']}: {taxon['name']}")
```

Learn more: [Species Encyclopedia](https://speciesfyi.com/species/) · [Taxonomic Ranks](https://speciesfyi.com/glossary/) · [Field Guides](https://speciesfyi.com/field-guides/)

### IUCN Conservation Status

The [IUCN Red List](https://www.iucnredlist.org/) is the world's most comprehensive inventory of the global conservation status of species. Each species is evaluated against quantitative criteria (population size, rate of decline, geographic range) and assigned one of 9 categories.

| Category | Code | Description |
|----------|------|-------------|
| **Extinct** | EX | No known living individuals |
| **Extinct in the Wild** | EW | Survives only in captivity |
| **Critically Endangered** | CR | Extremely high risk of extinction |
| **Endangered** | EN | Very high risk of extinction |
| **Vulnerable** | VU | High risk of extinction |
| **Near Threatened** | NT | Close to qualifying for a threatened category |
| **Least Concern** | LC | Low risk, widespread and abundant |
| **Data Deficient** | DD | Insufficient data to assess |
| **Not Evaluated** | NE | Not yet assessed against criteria |

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    # Search for endangered species
    results = api.search("endangered")
    for item in results["results"][:3]:
        print(f"{item['name']}: {item.get('conservation_status', 'N/A')}")
```

Learn more: [Species by Conservation Status](https://speciesfyi.com/species/) · [Biodiversity Glossary](https://speciesfyi.com/glossary/)

### Ecoregions and Biomes

An ecoregion is a large area of land or water with a geographically distinct assemblage of species, communities, and environmental conditions. The [WWF system](https://www.worldwildlife.org/biomes) divides the terrestrial world into **14 biomes** containing 867 ecoregions. SpeciesFYI catalogs 846 ecoregions with their biome classification, geographic extent, and associated species.

| Biome | Ecoregion Examples | Climate |
|-------|-------------------|---------|
| **Tropical Moist Forests** | Amazon, Congo Basin, Borneo lowlands | Hot, wet year-round |
| **Temperate Broadleaf Forests** | Appalachian, Western European | Moderate, seasonal |
| **Boreal Forests/Taiga** | Canadian boreal, Siberian taiga | Cold, long winters |
| **Tropical Grasslands** | Serengeti, Cerrado, Llanos | Hot, seasonal rainfall |
| **Deserts and Xeric Shrublands** | Sahara, Sonoran, Namib | Arid, extreme temperatures |
| **Tundra** | Arctic coastal, alpine meadows | Frozen, permafrost |

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    # Browse all 846 ecoregions
    ecoregions = api.list_ecoregions()
    print(ecoregions["count"])  # 846

    # Get details for a specific ecoregion
    eco = api.get_ecoregion("amazon-basin")
    print(eco["name"])  # Amazon Basin
```

Learn more: [Ecoregion Explorer](https://speciesfyi.com/ecoregions/) · [Habitat Guide](https://speciesfyi.com/habitats/)

### Habitats and Ecosystems

Habitats define where species live — from deep ocean trenches to alpine meadows. SpeciesFYI classifies habitats into hierarchical categories that map to species distribution patterns, helping researchers understand which environments support the greatest biodiversity.

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    # Browse habitat types
    habitats = api.list_habitats()
    for h in habitats["results"][:5]:
        print(h["name"])

    # Get species associated with a habitat
    habitat = api.get_habitat("coral-reef")
    print(habitat["name"])  # Coral Reef
```

Learn more: [Habitat Types](https://speciesfyi.com/habitats/) · [Guides](https://speciesfyi.com/guides/)

### Food Webs and Ecology

Food webs describe the feeding relationships in an ecosystem — who eats whom. Understanding trophic levels (producers, primary consumers, apex predators) reveals how energy flows through ecosystems and why the loss of a single species can cascade through an entire community.

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    # Explore food web relationships
    food_webs = api.list_food_webs()
    print(food_webs["count"])

    # Get a specific food web
    web = api.get_food_web("african-savanna")
    print(web["name"])  # African Savanna
```

Learn more: [Food Webs](https://speciesfyi.com/glossary/) · [Field Guides](https://speciesfyi.com/field-guides/)

## Command-Line Interface

```bash
pip install "speciesfyi[cli]"

speciesfyi search "bald eagle"     # Search across all species and taxa
```

## MCP Server (Claude, Cursor, Windsurf)

Add species data to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "speciesfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "speciesfyi": {
            "command": "uvx",
            "args": ["--from", "speciesfyi[mcp]", "python", "-m", "speciesfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    species = api.list_species()          # Browse all 49,112 species
    taxa = api.list_taxa()                # Browse 17,982 taxa
    ecoregions = api.list_ecoregions()    # Browse 846 ecoregions
    results = api.search("polar bear")    # Full-text search
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/species/` | List all species |
| GET | `/api/v1/species/{slug}/` | Species detail |
| GET | `/api/v1/taxa/` | List all taxa |
| GET | `/api/v1/taxa/{slug}/` | Taxon detail |
| GET | `/api/v1/ecoregions/` | List all ecoregions |
| GET | `/api/v1/ecoregions/{slug}/` | Ecoregion detail |
| GET | `/api/v1/habitats/` | List all habitats |
| GET | `/api/v1/habitats/{slug}/` | Habitat detail |
| GET | `/api/v1/ranks/` | List taxonomic ranks |
| GET | `/api/v1/countries/` | List countries |
| GET | `/api/v1/food-webs/` | List food webs |
| GET | `/api/v1/discoveries/` | List species discoveries |
| GET | `/api/v1/field-guides/` | List field guides |
| GET | `/api/v1/glossary/` | List glossary terms |
| GET | `/api/v1/guides/` | List guides |
| GET | `/api/v1/search/?q={query}` | Search across all content |

```bash
curl -s "https://speciesfyi.com/api/v1/species/?limit=3"
```

Full API documentation at [speciesfyi.com/developers/](https://speciesfyi.com/developers/).
OpenAPI 3.1.0 spec: [speciesfyi.com/api/openapi.json](https://speciesfyi.com/api/openapi.json).

## API Reference

| Function | Description |
|----------|-------------|
| `SpeciesFYI()` | Create API client (`base_url`, `timeout`) |
| `list_species(**params)` | List all species |
| `get_specy(slug)` | Get species detail |
| `list_taxa(**params)` | List all taxa |
| `get_taxa(slug)` | Get taxon detail |
| `list_ecoregions(**params)` | List all ecoregions |
| `get_ecoregion(slug)` | Get ecoregion detail |
| `list_habitats(**params)` | List all habitats |
| `get_habitat(slug)` | Get habitat detail |
| `list_ranks(**params)` | List taxonomic ranks |
| `list_countries(**params)` | List countries |
| `list_food_webs(**params)` | List food webs |
| `list_discoveries(**params)` | List species discoveries |
| `list_field_guides(**params)` | List field guides |
| `list_glossary(**params)` | List glossary terms |
| `list_guides(**params)` | List guides |
| `search(query)` | Search across all content |

## Learn More About Species

- **Browse**: [Species Encyclopedia](https://speciesfyi.com/species/) · [Taxonomic Tree](https://speciesfyi.com/taxa/) · [Ecoregions](https://speciesfyi.com/ecoregions/)
- **Reference**: [Habitats](https://speciesfyi.com/habitats/) · [Countries](https://speciesfyi.com/countries/) · [Discoveries](https://speciesfyi.com/discoveries/)
- **Guides**: [Glossary](https://speciesfyi.com/glossary/) · [Guides](https://speciesfyi.com/guides/) · [Field Guides](https://speciesfyi.com/field-guides/)
- **API**: [REST API Docs](https://speciesfyi.com/developers/) · [OpenAPI Spec](https://speciesfyi.com/api/openapi.json)

## Nature FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — living organisms, wildlife, and natural history.

| Package | PyPI | Description |
|---------|------|-------------|
| **speciesfyi** | [PyPI](https://pypi.org/project/speciesfyi/) | **49,112 species, 17,982 taxa, 846 ecoregions — [speciesfyi.com](https://speciesfyi.com/)** |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | 11,251 birds, 40 orders, 258 families — [birdfyi.com](https://birdfyi.com/) |
| fishfyi | [PyPI](https://pypi.org/project/fishfyi/) | 78 fish species, 48 orders, 188 families — [fishfyi.com](https://fishfyi.com/) |
| plantfyi | [PyPI](https://pypi.org/project/plantfyi/) | 379,774 plants, 734 families, 50 orders — [plantfyi.com](https://plantfyi.com/) |
| dinofyi | [PyPI](https://pypi.org/project/dinofyi/) | 6,142 dinosaurs, 15 periods, 198 countries — [dinofyi.com](https://dinofyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| **speciesfyi** | [PyPI](https://pypi.org/project/speciesfyi/) | — | Species taxonomy & biodiversity — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | — | Bird species encyclopedia — [birdfyi.com](https://birdfyi.com/) |
| fishfyi | [PyPI](https://pypi.org/project/fishfyi/) | — | Fish species & marine biology — [fishfyi.com](https://fishfyi.com/) |
| plantfyi | [PyPI](https://pypi.org/project/plantfyi/) | — | Plant taxonomy & cultivation — [plantfyi.com](https://plantfyi.com/) |
| dinofyi | [PyPI](https://pypi.org/project/dinofyi/) | — | Dinosaur paleontology & fossil record — [dinofyi.com](https://dinofyi.com/) |

## License

MIT
