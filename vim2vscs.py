import json
import os
import argparse
import time
from tqdm import tqdm

def convert_snippet_to_vscode(snippet_file, output_dir):
    """
    Converts a single .snippet file into a VS Code JSON snippet file.

    Args:
        snippet_file (str): Path to the .snippet file.
        output_dir (str): Directory where the converted JSON file will be saved.
    """
    snippets = {}
    with open(snippet_file, "r") as file:
        lines = file.readlines()

    current_snippet = {}
    for line in lines:
        line = line.strip()

        # Detect the start of a snippet
        if line.startswith("snippet"):
            parts = line.split(" ", 2)
            trigger = parts[1] if len(parts) > 1 else "unknown"
            description = parts[2].strip('"') if len(parts) > 2 else "No description"
            current_snippet = {
                "prefix": trigger,
                "body": [],
                "description": description
            }

        # Add body lines
        elif current_snippet and line != "endsnippet":
            current_snippet["body"].append(line)

        # End of the snippet
        elif line == "endsnippet":
            snippets[current_snippet["description"]] = current_snippet

    # Output JSON file name (based on the .snippet file name)
    output_file = os.path.join(output_dir, f"{os.path.basename(snippet_file).replace('.snippet', '.json')}")

    # Write to the output JSON file
    with open(output_file, "w") as out_file:
        json.dump(snippets, out_file, indent=4)

    print(f"Converted: {snippet_file} -> {output_file}")


def bulk_convert_snippets(input_dir, output_dir):
    """
    Converts all .snippet files in a directory to VS Code JSON format.

    Args:
        input_dir (str): Directory containing .snippet files.
        output_dir (str): Directory where converted JSON files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    snippet_files = [f for f in os.listdir(input_dir) if f.endswith(".snippet")]

    if not snippet_files:
        print(f"No .snippet files found in {input_dir}")
        return

    # Initialize progress tracking
    total_snippets = len(snippet_files)
    print(f"Total .snippet files to process: {total_snippets}")

    start_time = time.time()

    # Use tqdm for progress bar
    for i, snippet_file in enumerate(tqdm(snippet_files, desc="Processing snippets", unit="file")):
        snippet_file_path = os.path.join(input_dir, snippet_file)
        convert_snippet_to_vscode(snippet_file_path, output_dir)

        # Print time remaining estimates every 10 snippets processed
        if (i + 1) % 10 == 0 or (i + 1) == total_snippets:
            elapsed_time = time.time() - start_time
            estimated_time_remaining = (elapsed_time / (i + 1)) * (total_snippets - (i + 1))
            print(f"Processed {i + 1}/{total_snippets} snippets. Time left: {format_time(estimated_time_remaining)}")

    total_time = time.time() - start_time
    print(f"All .snippet files have been converted. Total time: {format_time(total_time)}")


def format_time(seconds):
    """
    Formats time in seconds to a more readable format (hh:mm:ss).

    Args:
        seconds (float): The time in seconds.

    Returns:
        str: Formatted time string.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    # CLI Argument Parsing
    parser = argparse.ArgumentParser(description="Convert .snippet files to VS Code JSON format.")
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory containing .snippet files to convert."
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Directory where converted JSON files will be saved."
    )

    args = parser.parse_args()

    # Run bulk conversion
    bulk_convert_snippets(args.input_dir, args.output_dir)