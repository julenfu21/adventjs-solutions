import pytest

from solution import run_factory


def test_run_factory_returns_string():
    factory = [">>."]

    final_state = run_factory(factory)

    assert isinstance(final_state, str)

@pytest.mark.parametrize(
    "factory,expected_state", [
        ([">>."], "completed"),
        ([">>>"], "broken"),
        ([">><"], "loop"),
        (
            [
                ">>v",
                "..<"
            ],
            "completed"
        ),
        (
            [
                ">>v",
                "<<<"
            ],
            "broken"
        ),
        (
            [
                ">v.",
                "^.."
            ],
            "completed"
        ),
        (
            [
                "v.",
                "^."
            ],
            "loop"
        ),
        (["."], "completed"),
        (["^"], "broken"),
        (
            [
                "v",
                "^"
            ],
            "loop"
        )
    ]
)
def test_run_factory(factory, expected_state):
    final_state = run_factory(factory)

    assert final_state == expected_state
