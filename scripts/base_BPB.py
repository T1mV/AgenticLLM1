import pandas as pd
import matplotlib.pyplot as plt

# creating the figure containing the btw using the excel data created with help of base_eval.py
df = pd.read_excel("Curve_data.xlsx")

plt.plot(df["Step"], df["Train BPB"], label="Training BPB")
plt.plot(df["Step"], df["Val BPB"], label="Validation BPB")
plt.title("Training and Validation BPB during base training")
plt.xlabel("Model training steps")
plt.ylabel("Bits-per-Bytes (BPB)")
plt.legend()
plt.show()