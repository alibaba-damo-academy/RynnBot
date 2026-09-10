#!/usr/bin/env python3
"""
Convert STL files (ASCII or binary) to Wavefront OBJ format.

Usage:
    python stl_to_obj.py input.stl
    python stl_to_obj.py input.stl -o output.obj
    python stl_to_obj.py input.stl --no-normals
    python stl_to_obj.py input.stl --merge-vertices

No third-party dependencies required.
"""

import argparse
import struct
import sys
from pathlib import Path


def _looks_like_ascii_stl(path: Path) -> bool:
    """Heuristic: check if file content looks like an ASCII STL."""
    try:
        with open(path, "rb") as f:
            header = f.read(256)
        # ASCII STL starts with "solid " and contains facet/endsolid markers.
        text = header.decode("ascii", errors="ignore").lower()
        return text.startswith("solid") and ("facet normal" in text or "endsolid" in text)
    except OSError:
        return False


def parse_ascii_stl(path: Path):
    """Parse an ASCII STL file.

    Returns:
        vertices: list of (x, y, z) tuples, 3 per triangle
        normals:  list of (nx, ny, nz) tuples, 1 per triangle
    """
    vertices = []
    normals = []

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        current_normal = None
        for raw_line in f:
            line = raw_line.strip().lower()
            if line.startswith("facet normal"):
                parts = line.split()
                if len(parts) >= 5:
                    current_normal = tuple(float(parts[i]) for i in range(2, 5))
            elif line.startswith("vertex"):
                parts = line.split()
                if len(parts) >= 4:
                    vertex = tuple(float(parts[i]) for i in range(1, 4))
                    vertices.append(vertex)
                    if current_normal is not None and len(vertices) % 3 == 1:
                        normals.append(current_normal)

    return vertices, normals


def parse_binary_stl(path: Path):
    """Parse a binary STL file.

    Returns:
        vertices: list of (x, y, z) tuples, 3 per triangle
        normals:  list of (nx, ny, nz) tuples, 1 per triangle
    """
    vertices = []
    normals = []

    with open(path, "rb") as f:
        f.read(80)  # header
        tri_count = struct.unpack("<I", f.read(4))[0]

        for _ in range(tri_count):
            normal = struct.unpack("<3f", f.read(12))
            normals.append(tuple(normal))

            for _ in range(3):
                vertex = struct.unpack("<3f", f.read(12))
                vertices.append(tuple(vertex))

            f.read(2)  # attribute byte count (usually 0)

    return vertices, normals


def parse_stl(path: Path):
    """Auto-detect STL format and parse it."""
    if _looks_like_ascii_stl(path):
        return parse_ascii_stl(path)
    return parse_binary_stl(path)


def write_obj(vertices, normals, output_path: Path, write_normals: bool, merge_vertices: bool):
    """Write vertices and faces to an OBJ file."""

    if merge_vertices:
        # Merge identical vertices to reduce file size.
        # Preserves flat shading by duplicating vertex indices per triangle normal.
        unique = {}
        index_map = []
        positions = []

        for v in vertices:
            key = (round(v[0], 6), round(v[1], 6), round(v[2], 6))
            if key not in unique:
                unique[key] = len(positions)
                positions.append(v)
            index_map.append(unique[key])

        face_vertex_indices = []
        for i in range(0, len(index_map), 3):
            face_vertex_indices.append((index_map[i], index_map[i + 1], index_map[i + 2]))
    else:
        positions = vertices
        face_vertex_indices = [(i, i + 1, i + 2) for i in range(0, len(vertices), 3)]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Converted from STL by stl_to_obj.py\n")
        for v in positions:
            f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")

        if write_normals and normals:
            for n in normals:
                f.write(f"vn {n[0]:.6f} {n[1]:.6f} {n[2]:.6f}\n")

        for tri_idx, (i1, i2, i3) in enumerate(face_vertex_indices):
            # OBJ indices are 1-based.
            v1, v2, v3 = i1 + 1, i2 + 1, i3 + 1
            if write_normals and normals:
                ni = tri_idx + 1
                f.write(f"f {v1}//{ni} {v2}//{ni} {v3}//{ni}\n")
            else:
                f.write(f"f {v1} {v2} {v3}\n")


def main():
    parser = argparse.ArgumentParser(description="Convert STL files to OBJ format")
    parser.add_argument("input", help="Input STL file path")
    parser.add_argument("-o", "--output", help="Output OBJ file path (default: same name with .obj)")
    parser.add_argument("--no-normals", action="store_true", help="Do not write facet normals")
    parser.add_argument("--merge-vertices", action="store_true",
                        help="Merge duplicate vertices to reduce file size")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path.with_suffix(".obj")

    print(f"Reading {input_path} ...")
    vertices, normals = parse_stl(input_path)

    if len(vertices) % 3 != 0:
        print(f"Warning: vertex count {len(vertices)} is not a multiple of 3", file=sys.stderr)

    print(f"Writing {output_path} ...")
    write_obj(vertices, normals, output_path,
              write_normals=not args.no_normals,
              merge_vertices=args.merge_vertices)

    print(f"Done. Triangles: {len(vertices) // 3}")


if __name__ == "__main__":
    main()
