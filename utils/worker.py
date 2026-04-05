import threading
from scanner import full_scan
import json
import time

class ScanWorker(threading.Thread):
    """
    Threaded worker for scanning a single target
    """
    def __init__(self, target, results_file="data/results.json"):
        super().__init__()
        self.target = target
        self.results_file = results_file

    def run(self):
        print(f"[Worker] Scanning target: {self.target}")
        result = full_scan(self.target)
        print(f"[Worker] Scan completed: {self.target}")

        # Append result safely
        try:
            with threading.Lock():
                try:
                    with open(self.results_file, "r") as f:
                        data = json.load(f)
                except Exception:
                    data = []

                data.append(result)

                with open(self.results_file, "w") as f:
                    json.dump(data, f, indent=4)
        except Exception as e:
            print(f"[Worker] Failed to save results: {str(e)}")


def run_workers(targets):
    """
    Run multiple ScanWorker threads in parallel
    """
    threads = []

    for t in targets:
        worker = ScanWorker(t)
        worker.start()
        threads.append(worker)
        time.sleep(0.2)  # small delay to avoid server overload

    for t in threads:
        t.join()

    print("[Worker] All targets scanned.")
