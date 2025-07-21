import os


def log_processing(log_file: str) -> None:
    """
    Compress consecutive identical log lines with a counter.
    For example:
    ["Error", "Error", "OK", "OK", "OK", "Error"]
    ➝ ["Error x2", "OK x3", "Error x1"]
    """
    lines = file_to_list(log_file)
    n = len(lines)
    if n == 0:
        return
    processed = []
    counter = 1
    for i in range(1, n):
        if lines[i] == lines[i - 1]:
            counter += 1
        else:
            processed.append(f"{lines[i - 1]} x{counter}")
            counter = 1
    processed.append(f"{lines[-1]} x{counter}")
    list_to_file(processed, "logs_processed.txt")
    print(
        f"Processed logs saved to {
            os.path.join('assets', 'logs_processed.txt')
            }"
    )


def file_to_list(file_name: str) -> list[str]:
    path = os.path.join("assets", file_name)
    if not os.path.exists(path):
        print("File does not exist in the file system", path)
        return []
    with open(path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def list_to_file(list: list[str], file_name: str) -> None:
    path = os.path.join("assets", file_name)
    with open(path, "w") as file:
        for line in list:
            file.write(line + "\n")
