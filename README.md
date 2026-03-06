# speciesfyi

Species taxonomy and biodiversity API client — [speciesfyi.com](https://speciesfyi.com)

## Install

```bash
pip install speciesfyi
```

## Quick Start

```python
from speciesfyi.api import SpeciesFYI

with SpeciesFYI() as api:
    results = api.search("eagle")
    print(results)
```

## License

MIT
