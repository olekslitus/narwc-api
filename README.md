# API for North Atlantic Right Whale Catalog (unofficial)

`narwc-api` is a Python library to access [North Atlantic Right Whale Catalog](https://rwcatalog.neaq.org).
This library enables you to access the whales from the catalog in your Python applications.

## Install
```shell
$ pip install narwc-api
```

## Simple Demo
```python
import narwc

for whale in narwc.Catalog.whales():
    print(f'Whale id: {whale.id}, name: {whale.name()}')
```

## Documentation
WIP

## Development
### Contributing
Long-term discussion and bug reports are maintained via GitHub Issues. Code review is done via GitHub Pull Requests.