from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.auth.auth import get_current_user
from app.database import get_db
from app.models import Workout
from app.schemas import WorkoutOut, WorkoutCreate

router = APIRouter(prefix="/workouts")

@router.post("/", response_model=WorkoutOut)
def create_workout(workout: WorkoutCreate,
                   db: Session = Depends(get_db),
                   current_user = Depends(get_current_user)):

    db_workout = Workout(
        name = workout.name,
        description = workout.description,
        user_id = current_user.id
    )

    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)

    return db_workout


@router.get("/", response_model=list[WorkoutOut])
def get_workouts(current_user = Depends(get_current_user),
                 db: Session = Depends(get_db),
                 skip: int = Query(0, ge=0),
                 limit: int = Query(10, ge=1, le=100)):

    workouts = db.query(Workout).filter(Workout.user_id == current_user.id).offset(skip).limit(limit).all()

    return workouts


@router.put("/{workout_id}", response_model=WorkoutOut)
def update_workout(workout_update: WorkoutCreate,
                   workout_id: int,
                   current_user = Depends(get_current_user),
                   db: Session = Depends(get_db)):

        workout_db = db.query(Workout).filter(Workout.id == workout_id).first()

        if not workout_db:
            raise HTTPException(404, detail="does not exist")

        if not current_user.id == workout_db.user_id:
            raise HTTPException(403, detail="unauthorised")

        workout_db.name = workout_update.name
        workout_db.description = workout_update.description

        db.commit()
        db.refresh(workout_db)

        return workout_db


@router.delete("/{workout_id}")
def delete_workout(workout_id: int,
                   current_user = Depends(get_current_user),
                   db: Session = Depends(get_db)):

    workout_to_delete = db.query(Workout).filter(Workout.id == workout_id).first()

    if not workout_to_delete:
        raise HTTPException(404, "workout does not exist")

    if not workout_to_delete.user_id == current_user.id:
        raise HTTPException(403, detail="unauthorised")

    db.delete(workout_to_delete)
    db.commit()

    return {"message": "workout deleted"}
