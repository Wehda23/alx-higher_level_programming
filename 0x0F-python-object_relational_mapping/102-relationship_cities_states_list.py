#!/usr/bin/python3
"""List Stats and informations"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main() -> None:
    """Main Function"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in (
        session.query(City, State)
        .join(State, State.id == City.state_id)
        .order_by(City.id)
    ):
        print("{}: {} -> {}".format(city.id, city.name, state.name))


if __name__ == "__main__":
    main()
