import pytest

from solution import run_factory


def test_run_factory_returns_string():
    factory = [">>."]

    final_state = run_factory(factory)

    assert isinstance(final_state, str)

@pytest.mark.parametrize(
    "factory,expected_state", [
        pytest.param([">>."], "completed", id="test-2"),
        pytest.param([">>>"], "broken", id="test-3"),
        pytest.param([">><"], "loop", id="test-4"),
        pytest.param(
            [
                ">>v",
                "..<"
            ],
            "completed",
            id="test-5"
        ),
        pytest.param(
            [
                ">>v",
                "<<<"
            ],
            "broken",
            id="test-6"
        ),
        pytest.param(
            [
                ">v.",
                "^.."
            ],
            "completed",
            id="test-7"
        ),
        pytest.param(
            [
                "v.",
                "^."
            ],
            "loop",
            id="test-8"
        ),
        pytest.param(["."], "completed", id="test-9"),
        pytest.param(["^"], "broken", id="test-10"),
        pytest.param(
            [
                "v",
                "^"
            ],
            "loop",
            id="test-11"
        )
    ]
)
def test_run_factory(factory, expected_state):
    final_state = run_factory(factory)

    assert final_state == expected_state
