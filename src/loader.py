import kagglehub

def load_data():
    path = kagglehub.dataset_download("mathchi/diabetes-data-set")
    print("Path to dataset files:", path)
    return path

if __name__ == "__main__":
    load_data()