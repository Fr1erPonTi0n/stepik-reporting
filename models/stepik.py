from typing import Union
from pydantic import BaseModel, RootModel


class Lesson(BaseModel):
    id: int
    steps: list[int]
    title: str


class LessonResponse(BaseModel):
    meta: dict
    lessons: list[Lesson]


class Block(BaseModel):
    name: str
    text: str


class Step(BaseModel):
    id: int
    block: Block


class StepResponse(BaseModel):
    meta: dict
    steps: list[Step]


class CodeProblem(BaseModel):
    title: str
    description: list[str]


class CodeReply(BaseModel):
    code: str
    language: str


class SqlReply(BaseModel):
    solve_sql: str


class Reply(RootModel):
    root: Union[CodeReply, SqlReply, dict]


class Submission(BaseModel):
    id: int
    status: str
    reply: Reply


class SubmissionResponse(BaseModel):
    meta: dict
    submissions: list[Submission]


class CodeSolution(BaseModel):
    title: str
    description: list[str]
    img_path: str


class Course(BaseModel):
    id: int
    sections: list[int]


class CoursesResponse(BaseModel):
    meta: dict
    courses: list[Course]


class Section(BaseModel):
    id: int
    units: list[int]
    title: str


class SectionsResponse(BaseModel):
    meta: dict
    sections: list[Section]


class Unit(BaseModel):
    id: int
    lesson: int


class UnitsResponse(BaseModel):
    meta: dict
    units: list[Unit]
