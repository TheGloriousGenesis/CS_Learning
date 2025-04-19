# FastApi

Produces interactive API docs (provided by Swagger UI or ReDoc)

Looking into broken links in API docs

Created a little diagram to solidify my understanding regarding the architecture and how data is being processed around.


## Glossary

|   Phrase    |                            Definition                             |
|:-----------:|:-----------------------------------------------------------------:|
|   Schema    |             non code abstract definition of something             |
| API Schema  |           OpenAPI specific schema they are following.             |
|  Open API   | Describes a language agnostic interface description for HTTP APIs |
| Data Schema |               Shape of some data, e.h JSON content                |

> [!NOTE]
> RESTful API is a type of webservice that uses HTTP methods and URIs to interact with resources while Open API
> is a specfication for designing and documenting RESTful APIs

## Intro

Code for FastApi should be in `main.py` and runs with `uvicorn`

`uvicorn` is a server that runs code

`/docs` -> Swagger UI
`/redoc` -> ReDoc
`/openapi.json` -> JSON Schema of generated API docs

To create a FastAPI app use the following lines of code

```python
from fastapi import FastApi

app = FastApi()
```


## Setting up jaegar tracing with fastapi

```python
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# set up tracing https://uptrace.dev/get/instrument/opentelemetry-fastapi.html#opentelemetry-sdk , https://guitton.co/posts/fastapi-monitoring


provider = TracerProvider()
exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
processor = BatchSpanProcessor(exporter)
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)

#Todo: issue with finding /docs path with root_path included for some reason
app = FastAPI(
    root_path=traefik_root_path,
)

FastAPIInstrumentor.instrument_app(app)

```
