def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
    return data


if __name__ == "__main__":
    text = load_data("data/sample.txt")
    print("Loaded Data:\n", text)