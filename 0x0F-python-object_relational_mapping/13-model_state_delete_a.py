#!/usr/bin/python3
"""List Stats and informations"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main() -> None:
    """Main function to run scripts"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
