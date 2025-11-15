import os
import re
import time
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, stdev

from run import run_day


@contextmanager
def suppress_output():
    with open(os.devnull, "w") as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


@dataclass
class PerfMeasurement:
    t_sample: list[float]

    def __post_init__(self):
        print(
            f"Measurement created: {len(self.t_sample)} samples, mean = {mean(self.t_sample)}, std = {stdev(self.t_sample)}"
        )

    @property
    def mean(self) -> float:
        return float(mean(self.t_sample))

    def __add__(self, other: "PerfMeasurement") -> "PerfMeasurement":
        return PerfMeasurement(
            [t1 + t2 for t1, t2 in zip(self.t_sample, other.t_sample)]
        )

    def __str__(self) -> str:
        std = stdev(self.t_sample)
        return f"{round(self.mean, 2)} ± {round(std, 2)}"


if __name__ == "__main__":
    days_perf: list[tuple[int, tuple[PerfMeasurement, PerfMeasurement]]] = []
    n_samples = 10
    for day in range(1, 26):
        try:
            print(f"Measuring day {day}...")
            sample_1: list[float] = []
            sample_2: list[float] = []
            measure_start = time.time()
            for _ in range(n_samples):
                with suppress_output():
                    t1, t2 = run_day(
                        day,
                        parts_to_run=[1, 2],
                        example=False,
                        debug=False,
                    )
                if t1 is None:
                    print(f"Error measuring day {day} pt 1, skipping realization")
                    continue
                if t2 is None:
                    print(f"Error measuring day {day} pt 2, skipping realization")
                    continue
                sample_1.append(t1)
                sample_2.append(t2)
            days_perf.append(
                (
                    day,
                    (
                        PerfMeasurement(sample_1),
                        PerfMeasurement(sample_2),
                    ),
                )
            )
        except Exception as e:
            print(f"Error measuring day {day}, ignoring: {e!r}")

    # results formatting
    headers = [
        "**Day**",
        "**Part 1**, msec",
        "**Part 2**, msec",
        "**Total**, msec",
    ]
    markdown_table = [
        headers,
        ["---:"] + [":---:"] * (len(headers) - 2) + ["---"],
    ]
    total_part_1 = PerfMeasurement([0.0] * n_samples)
    total_part_2 = PerfMeasurement([0.0] * n_samples)

    for day, (part_1, part_2) in days_perf:
        markdown_table.append(
            [str(day), str(part_1), str(part_2), str(part_1 + part_2)]
        )
        total_part_1 = total_part_1 + part_1
        total_part_2 = total_part_2 + part_2
    total_both_parts = total_part_1 + total_part_2

    markdown_table.append(
        [
            "All days",
            str(total_part_1),
            str(total_part_2),
            str(total_both_parts),
        ]
    )

    readme_file = Path(__file__).parent / "README.md"
    readme = readme_file.read_text()
    readme = re.sub(
        (
            "(?<="
            + re.escape("<!-- generated table start -->")
            + ")(.*)(?="
            + re.escape("<!-- generated table end -->")
            + ")"
        ),
        "\n" + "\n".join([" | ".join(row) for row in markdown_table]) + "\n",
        readme,
        flags=re.MULTILINE | re.DOTALL,
    )
    readme_file.write_text(readme)
    print("Done")
