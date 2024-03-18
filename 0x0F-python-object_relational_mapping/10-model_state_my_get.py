#!/usr/bin/python3
"""List Stats and informations"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main() -> None:
    """Main Function To run script"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    filtered_states = states.filter(State.name == argv[4])
    orederd_states = filtered_states.order_by(State.id).all()
    if orederd_states:
        print("{}".format(orederd_states[0].id))
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    main()
