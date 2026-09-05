# CPU Performance Benchmark

Ferramenta de benchmark de CPU para análise de throughput em pipelines de dados.
Mede operações vetoriais e throughput de memória em runners CI.

## Uso
```bash
pip install -r requirements.txt
python cpu_bench.py
```

## Métricas
- `cpu_bench.py` — throughput float + teste de memória
- Workflow `bench` roda 3 shards em paralelo para média estável.
