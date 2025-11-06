import pandas as pd
import os
from my_app.models import Product


def upload_products_from_csv(file_path):
    """
    Upload products from a CSV file in chunks(For memory management),
    ensuring that 'price' and 'stock' fields are non-negative.
    """
    df = pd.read_csv(file_path, chunksize=1000, dtype={
        'name': str,
        'category': str,
        'price': float,
        'stock': int
    })
    for i, chunk in enumerate(df):
        chunk = chunk.drop('created_at', axis=1, errors='ignore')
        chunk.loc[chunk['price'] < 0, 'price'] = 0
        chunk.loc[chunk['stock'] < 0, 'stock'] = 0
        Product.objects.bulk_create(
            [Product(**row) for index, row in chunk.iterrows()]
        )
        print(f"Uploaded chunk {i + 1}")


file_path = os.path.join(os.path.dirname(__file__), 'large_dataset.csv')
upload_products_from_csv(file_path)
print("Product upload completed.")
