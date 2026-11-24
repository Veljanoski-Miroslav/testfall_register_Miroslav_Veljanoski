
import pytest



from model.register import Register
from service.register_testcase import RegisterTestcase


@pytest.fixture
def service() -> RegisterTestcase:
    return RegisterTestcase()


def test_add_register__should_save_and_return_register_when_valid(service: RegisterTestcase):
    # arrange
    testfall_id = 1
    testfall_name = "Inloggningstest"
    testfall_description = "Testar att användare kan logga in med giltiga uppgifter"

    # act
    result = service.add_register(testfall_id, testfall_name, testfall_description)

    # assert
    assert isinstance(result, Register)
    assert result.testfall_id == 1
    assert result.testfall_name == "Inloggningstest"
    assert result.testfall_description == "Testar att användare kan logga in med giltiga uppgifter"
    assert len(service.registers) == 1
    assert service.registers[0] == result


@pytest.mark.parametrize(
    "testfall_id, testfall_name, testfall_description, expected_error",
    [
        (1, "", "Beskrivning", "Testfall Namn kan inte vara tomt."),
        (1, "Inloggningstest", "", "Testfall Beskrivning kan inte vara tomt."),
    ],
)
def test_add_register__should_validate_and_raise_error_on_missing_values(
    service: RegisterTestcase,
    testfall_id: int,
    testfall_name: str,
    testfall_description: str,
    expected_error: str,
):
    # arrange & act & assert
    with pytest.raises(ValueError) as exc_info:
        service.add_register(testfall_id, testfall_name, testfall_description)

    assert str(exc_info.value) == expected_error
    assert len(service.registers) == 0
