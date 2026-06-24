from src.config import DATA_PATH

dataset = []
with open(DATA_PATH, "r") as file:
    dataset = file.readlines()
    # print(len(dataset))

if __name__ == "__main__":
    print(dataset)