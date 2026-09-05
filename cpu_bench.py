"""CPU throughput bench — operações vetoriais + memória."""
import time
import numpy as np
import psutil


def bench(n=80, iters=15):
    t0 = time.time()
    acc = 0.0
    for _ in range(iters):
        a = np.random.rand(n, n).astype(np.float32)
        b = np.random.rand(n, n).astype(np.float32)
        c = (a * b).sum() + (a + b).mean()
        acc += float(c)
    dt = time.time() - t0
    mem = psutil.virtual_memory().percent
    print(f"{iters} ops {n}x{n} em {dt:.2f}s mem={mem:.0f}% acc={acc:.1f}")


if __name__ == "__main__":
    bench()
