import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from bs4 import BeautifulSoup
import sympy
from faker import Faker
import openpyxl
import lxml

# 1. requests
try:
    response = requests.get("https://httpbin.org/get")
    print("Requests test:", response.status_code)
except Exception as e:
    print("Requests error:", e)

# 2. numpy
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("Numpy test (mean):", arr.mean())
except Exception as e:
    print("Numpy error:", e)

# 3. pandas
try:
    df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})
    print("Pandas test (head):\n", df.head())
except Exception as e:
    print("Pandas error:", e)

# 4. Pillow (PIL)
try:
    img = Image.new("RGB", (100, 100), color="blue")
    img.show()  # Відкриває нове вікно з картинкою
    print("Pillow test: Image created and shown")
except Exception as e:
    print("Pillow error:", e)

# 5. Faker
try:
    fake = Faker()
    print("Faker test: Name:", fake.name(), "| Email:", fake.email())
except Exception as e:
    print("Faker error:", e)
