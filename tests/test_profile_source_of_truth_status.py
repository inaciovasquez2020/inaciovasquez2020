import subprocess
import sys

def test_profile_source_of_truth_status_guard_passes():
    subprocess.run(
        [sys.executable, "scripts/check_profile_source_of_truth_status.py"],
        check=True,
    )
