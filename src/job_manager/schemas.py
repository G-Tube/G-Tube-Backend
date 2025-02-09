from enum import Enum


class JobStatus(Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    PROCESSING = "processing"
    COMPLETED = "completed"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
