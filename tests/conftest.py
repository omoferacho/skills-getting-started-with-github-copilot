import pytest
import copy
from fastapi.testclient import TestClient
from src.app import app, activities as original_activities


@pytest.fixture
def activities_copy():
    """Provide a fresh copy of activities for each test"""
    return copy.deepcopy(original_activities)


@pytest.fixture
def client(activities_copy, monkeypatch):
    """Provide a test client with isolated activities database"""
    # Replace the activities in the app with our copy
    monkeypatch.setattr("src.app.activities", activities_copy)
    return TestClient(app)
