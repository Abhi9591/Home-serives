from app.database import SessionLocal
from app.models.service import Service

db = SessionLocal()

if not db.query(Service).first():
    db.add_all([
        Service(name="AC Repair", description="AC installation & repair", price=499),
        Service(name="Salon at Home", description="Professional beauty services", price=799),
        Service(name="Plumbing", description="Leak fixing & pipe repair", price=299),
    ])
    db.commit()

db.close()
