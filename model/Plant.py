class Plant:
    def __init__(self, label):
        self.label = label
        self.recommondation = None
        if self.label == "Healthy":
            self.recommondation = "Plant is Healthy so no medicine is required"
        elif self.label == "Powdery":
            self.recommondation = "Sulfur-based fungicide is recommended as plant is suffering from Powdery mildew disease";
        elif self.label == "Rust":
            self.recommondation = "Copper-based fungicide is recommended as plant is suffering from Rust disease";
