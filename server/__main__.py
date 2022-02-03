
import os

from server import initiate_server

HOST = os.getenv("IP_ADDRESS") or "localhost"


def main():
    """
    Main function for server
    """
    app = initiate_server()
    app.run(host=HOST, port=8080, debug=True)


if __name__ == "__main__":
    main()
