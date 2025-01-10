# track_kids_measurements_backend

# run the backend
uvicorn app.main:app --reload

# Summary of the Alembic Workflow
Model Changes: Modify your SQLAlchemy models (add columns, rename tables, etc.).
Generate Migration: Run alembic revision --autogenerate -m "Some message".
Review Migration: Check the generated script in migrations/versions/.
Apply Migration: Run alembic upgrade head to apply it to your database.

# By using Alembic, you gain:
Version History: Each migration is timestamped and explains a single schema change.
Rollback Ability: Alembic generates downgrade() methods, letting you revert your database if needed.
Team Collaboration: Multiple developers can write and share migrations without overwriting each other’s work.




