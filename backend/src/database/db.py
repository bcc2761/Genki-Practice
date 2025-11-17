from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import models

def get_challenge_quota(db: Session, user_id: str) -> models.ChallengeQuota:
    """Retrieve the ChallengeQuota for a given user_id."""
    return (db.query(models.ChallengeQuota)
        .filter(models.ChallengeQuota.user_id == user_id)
        .first())

def create_challenge_quota(db: Session, user_id: str):
    db_quota = models.ChallengeQuota(user_id=user_id)
    db.add(db_quota)
    db.commit() # write to database
    db.refresh(db_quota) # refresh instance with data from database
    return db_quota    

def reset_quota_if_needed(db: Session, quota: models.ChallengeQuota):
    """Reset the quota if last_reset_date is more than 24 hours ago."""
    now = datetime.now()
    if now - quota.last_reset_date >= timedelta(hours=24):
        quota.quota_remaining = 20
        quota.last_reset_date = now
        db.commit()
        db.refresh(quota)
    return quota

def create_challenge(
        db: Session, 
        chapter: int, 
        created_by: str, 
        title: str,
        options: str, 
        correct_answer_id: int, 
        explanation: str
    ):
    db_challenge = models.Challenge(
        chapter=chapter,
        created_by=created_by,
        title=title,
        options=options,
        correct_answer_id=correct_answer_id,
        explanation=explanation
    )
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge

def get_user_challenges(db: Session, user_id: str):
    """Retrieve all challenges created by a specific user."""
    return (db.query(models.Challenge)
        .filter(models.Challenge.created_by == user_id)
        .all()) # gives all the entries the user has created