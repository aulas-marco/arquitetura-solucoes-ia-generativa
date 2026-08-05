"""Observa, com OpenTelemetry local, a trajetória de requisição do Lume e da Aurora."""

from __future__ import annotations

import argparse
import json
import time
from urllib.request import Request, urlopen

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor


CASOS = {
    "lume": {
        "etapa_conhecimento": "consulta_indice_politicas_contestacao",
        "pergunta": "Resuma, com referências, a política de contestação aplicável ao caso C-4021.",
    },
    "aurora": {
        "etapa_conhecimento": "consulta_indice_politicas_campanha_e_ferramenta_leitura",
        "pergunta": "Prepare o dossiê de renegociação do contrato CT-9187, citando política vigente.",
    },
}

provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("plataforma.operacao")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--caso", choices=sorted(CASOS), required=True)
    args = parser.parse_args()
    caso = CASOS[args.caso]

    started = time.perf_counter()
    with tracer.start_as_current_span("entrada") as root:
        root.set_attribute("gen_ai.request.model", "boreal-local")
        root.set_attribute("boreal.produto", args.caso)
        with tracer.start_as_current_span("conhecimento") as knowledge:
            knowledge.set_attribute("boreal.etapa", caso["etapa_conhecimento"])
        with tracer.start_as_current_span("modelo"):
            request = Request(
                "http://localhost:4000/v1/chat/completions",
                data=json.dumps({
                    "model": "boreal-local",
                    "messages": [{"role": "user", "content": caso["pergunta"]}],
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
    print(f"PRODUTO: {args.caso}")
    print(f"DURACAO_MS: {(time.perf_counter() - started) * 1000:.0f}")
    print(f"RESPOSTA: {payload['choices'][0]['message']['content']}")


if __name__ == "__main__":
    main()
