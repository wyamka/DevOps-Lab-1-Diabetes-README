import kagglehub

def load_data():
    # Загружаем последнюю версию датасета о диабете
    path = kagglehub.dataset_download("mathchi/diabetes-data-set")
    print("Path to dataset files:", path)
    return path

if __name__ == "__main__":
    load_data()