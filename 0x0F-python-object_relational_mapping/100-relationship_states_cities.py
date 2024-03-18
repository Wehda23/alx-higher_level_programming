#!/usr/bin/python3
"""List Stats and informations"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main() -> None:
    """Main Script function"""
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
    new_state = State(name="California")
    session.add(new_state)
    session.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
