#!/usr/bin/env python3
"""
Example demonstrating how to generate a publication-ready APA 7 report in PDF format.
"""

import os
import sys

# Ensure local module is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apa7_pdf import build_apa7_document, compile_html_to_pdf


def main():
    print("=== Generating APA 7 Sample Report ===")

    title = "Empirical Analysis of Deep Learning Pipeline Latencies under Linux Kernel Subsystems"
    author = "ProgramaGrueso Research Group"
    institution = "Laboratory of Applied Computer Vision & Systems Engineering"

    abstract = (
        "This empirical report investigates latency variations in real-time facial feature extraction "
        "and loopback video streaming under modern Linux kernels. Utilizing hardware-accelerated "
        "video pipelines with v4l2loopback and vectorized spatial decimation, we quantify the impact "
        "of sub-sampling routines on inference overhead and visual quality metrics."
    )

    sections = [
        {
            "title": "Methodology",
            "paragraphs": [
                "The computational pipeline was evaluated across 1,000 continuous inference cycles on an "
                "isolated Linux workstation. Frames were captured via USB ADB transport directly from high-framerate "
                "sensor inputs and ingested through memory-mapped loopback nodes.",
                "To overcome spatial resolution bottlenecks inherent to single-pass models, an interleaved "
                "phase decimation strategy was applied, subdividing 256x256 facial patches into quad 128x128 matrices.",
            ],
        },
        {
            "title": "Discussion",
            "paragraphs": [
                "Observations indicate that vectorized NumPy array slicing introduces sub-millisecond overhead, "
                "rendering it negligible compared to neural network execution times on dedicated Tensor Cores. "
                "No temporal jitter or frame degradation was observed during continuous streaming tests."
            ],
        },
    ]

    tables = [
        {
            "number": "Table 1",
            "title": "Inference Latency and Reconstruction Metrics Across Sampling Methods",
            "headers": ["Method", "Resolution (px)", "Overhead (ms)", "Parity Check"],
            "rows": [
                ["Bicubic Downsampling", "128 x 128", "0.42", "Lossy (Filtered)"],
                ["GFPGAN Restoration", "512 x 512", "18.30", "Generative (Hallucinated)"],
                ["Interleaved Grid Sampling", "256 x 256", "0.75", "100% Lossless Parity"],
            ],
            "note": "All benchmarks measured on x86_64 architecture with 16 physical cores under Linux 6.x kernel.",
        }
    ]

    references = [
        "InsightFace Developers. (2023). <em>InSwapper: High-fidelity deep facial identity transfer</em>. InsightFace Research Repository.",
        "Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. <em>Cognitive Psychology</em>, 3(3), 430–454. https://doi.org/10.1016/0010-0285(72)90016-3",
        "OpenCV Team. (2024). <em>Open source computer vision library: Video I/O and v4l2 backend reference</em>. OpenCV Foundation.",
    ]

    html = build_apa7_document(
        title=title,
        author=author,
        institution=institution,
        abstract=abstract,
        sections=sections,
        tables=tables,
        references=references,
    )

    output_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sample_APA7_Report.pdf")
    generated_path = compile_html_to_pdf(html, output_pdf)
    print(f"[✓] Generated APA 7 compliant PDF successfully:")
    print(f"    Path: {generated_path}")
    print(f"    Size: {os.path.getsize(generated_path) / 1024:.1f} KB")


if __name__ == "__main__":
    main()
