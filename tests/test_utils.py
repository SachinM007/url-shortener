from app.utils import generate_short_id


def test_generate_short_id():
    short_id = generate_short_id()
    assert len(short_id) == 6
    assert short_id.isalnum()

