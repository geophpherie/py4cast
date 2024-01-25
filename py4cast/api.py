import requests

BASE_URL = "https://api.weather.gov"


def get_office_afd_products(office_id: str) -> list[str]:
    """Retrieves all available afd products for the given office.

    Args:
        office_id (str): forecast office ID

    Returns:
        list[str]: all available afd products
    """
    response = requests.get(f"{BASE_URL}/products/types/AFD/locations/{office_id}/")

    response.raise_for_status()

    return response.json().get("@graph", [])


def get_product(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}/")

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    p = get_office_afd_products("PQR")
    print(p)
