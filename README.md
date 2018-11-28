# Fluentd Log Handler

Python logging handler for Fluentd

## Requirements(Python Package)

- fluent-logger

## Installation

```bash
pip install fluentd_log_handler
```

## Example

```python
import logging
from fluentd_log_handler.handler import NeilFluentdHandler

handler = NeilFluentdHandler(tag='app.worker')

logger = logging.getLogger('neil')
logger.addHandler(handler)

logger.error({'task_name': '금융정보 조회', 'request_id': 1})
```
