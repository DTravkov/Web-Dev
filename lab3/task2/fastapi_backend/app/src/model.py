
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass
class TaskModel(Base):
    __tablename__ = 'tasks'
    task_name:Mapped[str] = mapped_column(primary_key=True)