from ...model import Type
from typing import List, Any, Optional


class Profile(Type):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_date: Optional[str] = None
    sex: Optional[str] = None
    user_id: Optional[int] = None
    id: Optional[int] = None
    contract_id: Optional[Any] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    snils: Optional[str] = None
    type: Optional[str] = None


class School(Type):
    id: Optional[int] = None
    name: Optional[str] = None
    short_name: Optional[str] = None
    county: Optional[Any] = None
    principal: Optional[Any] = None
    phone: Optional[Any] = None
    global_school_id: Optional[int] = None


class Group(Type):
    id: Optional[int] = None
    name: Optional[str] = None
    subject_id: Optional[int] = None
    is_fake: Optional[bool] = None


class Representative(Type):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_date: Optional[Any] = None
    sex: Optional[Any] = None
    user_id: Optional[Any] = None
    id: Optional[int] = None
    contract_id: Optional[Any] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    snils: Optional[str] = None
    type: Optional[Any] = None


class Child(Type):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_date: Optional[str] = None
    sex: Optional[str] = None
    user_id: Optional[int] = None
    id: Optional[int] = None
    contract_id: Optional[Any] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    snils: Optional[str] = None
    type: Optional[Any] = None
    school: Optional[School] = None
    class_name: Optional[str] = None
    class_level_id: Optional[int] = None
    class_unit_id: Optional[int] = None
    groups: Optional[List[Group]] = []
    representatives: Optional[List[Representative]] = []
    sections: Optional[List] = []
    sudir_account_exists: Optional[bool] = None
    sudir_login: Optional[Any] = None
    is_legal_representative: Optional[bool] = None
    parallel_curriculum_id: Optional[int] = None
    contingent_guid: Optional[str] = None
    enrollment_date: Optional[str] = None


class WebFamilyProfile(Type):
    profile: Optional[Profile] = None
    children: Optional[List[Child]] = None
    hash: Optional[str] = None
