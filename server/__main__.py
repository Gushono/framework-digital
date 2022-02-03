
import os

from server import initiate_server

HOST = os.getenv("IP_ADDRESS") or "127.0.0.1"


def main():
    """
    Main function for server
    """
    app = initiate_server()
    app.run(host=HOST, port=8080, debug=False)


if __name__ == "__main__":
    main()
