import requests

def extract_products():
    url = "https://labdados.com/produtos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    produtos = extract_products()
    print(f"Total de produtos extraídos: {len(produtos)}")