#!/usr/bin/python3
"""List Stats and informations"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main() -> None:
    """Main function to run script"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State)
    filtered_data = data.filter(State.name.like("%a%"))
    ordered_data = filtered_data.order_by(State.id).all()
    for state in ordered_data:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    main()
