from ext.db import session
from ext.db.models import *
from datetime import datetime
from sqlalchemy import update


stmt = (
    update(Local).
    where(Local.latitude == -694.5280151367188).
    values(latitude=-69.45280)
)

q = session.query(Herpto)
