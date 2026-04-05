import threading
from scanner import full_scan

def distributed_scan(targets):
    """
    Runs scans in multiple threads (safe)
    """
    results = []

    def worker_func(t):
        res = full_scan(t)
        results.append(res)

    threads = []
    for t in targets:
        thread = threading.Thread(target=worker_func, args=(t,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results
