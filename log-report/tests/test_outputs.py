import json
from pathlib import Path

def load_report():
    assert Path("/app/report.json").exists(), "report.json not found"
    with Path("/app/report.json").open() as f:
        return json.load(f)

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"

def test_report_schema():
    """The report is valid JSON with valid fields"""
    report = load_report()
    assert isinstance(report, dict), "invalid json"
    
    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }

    assert isinstance(report["total_requests"], int)
    assert isinstance(report["unique_ips"], int)
    assert isinstance(report["top_path"], str)
    
def test_report_values():
    """The report contains the correct summary values."""
    report = load_report()

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"