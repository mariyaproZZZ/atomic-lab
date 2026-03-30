from app import validate_email, get_user_status, process_user_data


class TestValidateEmail:
    def test_valid_email(self):
        """GIVEN a valid email
        WHEN validate_email is called
        THEN returns True"""
        assert validate_email("test@example.com") is True

    def test_invalid_email_no_at(self):
        """GIVEN email without @
        WHEN validate_email is called
        THEN returns False"""
        assert validate_email("testexample.com") is False


class TestGetUserStatus:
    def test_adult_status(self):
        """GIVEN age 25
        WHEN get_user_status is called
        THEN returns 'adult'"""
        assert get_user_status(25) == "adult"

    def test_teen_status(self):
        """GIVEN age 15
        WHEN get_user_status is called
        THEN returns 'teen'"""
        assert get_user_status(15) == "teen"

    def test_child_status(self):
        """GIVEN age 5
        WHEN get_user_status is called
        THEN returns 'child'"""
        assert get_user_status(5) == "child"


class TestProcessUserData:
    def test_valid_user_data(self):
        """GIVEN valid user data
        WHEN process_user_data is called
        THEN returns processed data"""
        user = {"name": "Alice", "email": "ALICE@TEST.COM", "age": 30}
        result = process_user_data(user)
        assert result["name"] == "ALICE"
        assert result["email"] == "alice@test.com"
        assert result["status"] == "adult"

    def test_missing_email(self):
        """GIVEN user data without email
        WHEN process_user_data is called
        THEN returns error"""
        user = {"name": "Bob", "age": 20}
        result = process_user_data(user)
        assert result == {"error": "Invalid email"}

    def test_underage_user(self):
        """GIVEN user under 18
        WHEN process_user_data is called
        THEN returns error"""
        user = {"name": "Diana", "email": "diana@test.com", "age": 16}
        result = process_user_data(user)
        assert result == {"error": "Too young"}
