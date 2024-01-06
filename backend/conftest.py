import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
    print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))  # For debugging


@pytest.fixture(scope="session", autouse=True)
def verify_env_variables():
    required_vars = [
        "SUPABASE_URL",
        "SUPABASE_SERVICE_KEY",
        "OPENAI_API_KEY",
        "JWT_SECRET_KEY",
        "CELERY_BROKER_URL",
    ]
    if missing_vars := [var for var in required_vars if not os.getenv(var)]:
        missing_vars_str = ", ".join(missing_vars)
        pytest.fail(f"Required environment variables are missing: {missing_vars_str}")


@pytest.fixture(scope="module")
def client():
    from main import app

    return TestClient(app)


@pytest.fixture(scope="module")
def api_key():
    if API_KEY := os.getenv("CI_TEST_API_KEY"):
        return API_KEY
    else:
        raise ValueError(
            "CI_TEST_API_KEY environment variable not set. Cannot run tests."
        )
