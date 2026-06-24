import pytest
import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_logger import log_result

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    start = time.time()
    outcome = yield
    duration = round(time.time() - start, 2)
    report = outcome.get_result()

    if report.when == "call":
        status = "PASS" if report.passed else "FAIL"
        error = str(report.longrepr) if report.failed else None
        log_result(item.name, status, duration, error)