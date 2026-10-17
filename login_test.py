
def test_valid_login():
    username = "Jatin23IT125"
    password = "23it125"

    # Simulated login validation
    login_success = bool(username and password)

    assert login_success is True
    print("PASS: Valid login test")


def test_empty_username():
    username = ""
    password = "valid123"

    login_success = bool(username and password)

    assert login_success is False
    print("PASS: Empty username rejected")


if __name__ == "__main__":
    test_valid_login()
    test_empty_username()
