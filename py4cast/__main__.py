import argparse
import api


def main(office_id: str):
    print(f"Getting forecast for office {office_id}")
    products = api.get_office_afd_products(office_id=office_id)

    product = api.get_product(products[0]["id"])

    discussion = product["productText"]

    print(discussion)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="py4cast",
        description="Retrieves the Area Forecast Discussion for a given NWS forecast office.",
    )

    parser.add_argument(
        "office_id",
        help="NWS Forecast Office Id (https://www.weather.gov/srh/nwsoffices)",
    )

    args = parser.parse_args()

    main(args.office_id)
