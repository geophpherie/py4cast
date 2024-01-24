import argparse


def main(office_id: str):
    print(f"Getting forecast for office {office_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="py4cast",
        description="Retrieves the Area Forecast Discussion for a given forecast office.",
        epilog="-----------",
    )

    parser.add_argument(
        "office_id",
        help="Forecast Office Id (https://www.weather.gov/srh/nwsoffices)",
    )

    args = parser.parse_args()

    main(args.office_id)
