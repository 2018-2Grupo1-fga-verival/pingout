import pytest
from pingout.utils import validate_uuid
from uuid import UUID

def test_validate_uuid():
    wrong_uuid_string = '12e21e8474feaa930ii112o'
    right_uuid_string = '12e21e8474fe43c3a9909476ac899345'

    valueUUID = UUID(right_uuid_string, version=4)

    exceptionReturnValue = validate_uuid(wrong_uuid_string)
    rightReturnValue = validate_uuid(right_uuid_string)

    assert exceptionReturnValue == False
    assert rightReturnValue == True
    assert valueUUID.hex == right_uuid_string
