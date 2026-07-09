import pickle

model = pickle.load(open("model.pkl", "rb"))

print(hasattr(model, "classes_"))
print(hasattr(model, "class_count_"))
print(hasattr(model, "feature_count_"))