"""Gera uma chamada sintética pelo gateway e a observa com OpenTelemetry local."""

from __future__ import annotations

import json
import time
from urllib.request import Request, urlopen

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor


provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("boreal.operacao")


def main() -> None:
    started = time.perf_counter()
    with tracer.start_as_current_span("entrada") as root:
        root.set_attribute("gen_ai.request.model", "boreal-local")
        root.set_attribute("boreal.produto", "resumo-interno")
        with tracer.start_as_current_span("modelo"):
            request = Request(
                "http://localhost:4000/v1/chat/completions",
                data=json.dumps({
                    "model": "boreal-local",
                    "messages": [{"role": "user", "content": "Resuma o indicador sintético tr-202 em uma frase."}],
                    "temperature": 0.2,
                }).encode(),
                headers={"Content-Type": "application/json"},
            )
            with urlopen(request) as response:  # noqa: S310 - endpoint local do laboratório
                payload = json.loads(response.read())
        with tracer.start_as_current_span("saida") as output:
            output.set_attribute("boreal.resultado", "ok")
            output.set_attribute("boreal.tamanho_resposta", len(payload["choices"][0]["message"]["content"]))
        trace_id = format(root.get_span_context().trace_id, "032x")
    print(f"TRACE_ID: {trace_id}")
    print(f"DURACAO_MS: {(time.perf_counter() - started) * 1000:.0f}")
    print(f"RESPOSTA: {payload['choices'][0]['message']['content']}")


if __name__ == "__main__":
    main()
