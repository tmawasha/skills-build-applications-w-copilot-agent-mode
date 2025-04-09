from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Create test data
# Users
user1 = User.objects.create(email="user1@example.com", name="User One", age=25)
user2 = User.objects.create(email="user2@example.com", name="User Two", age=30)

# Teams
team1 = Team.objects.create(name="Team Alpha")
team1.members.add(user1, user2)

# Activities
Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-01")
Activity.objects.create(user=user2, activity_type="Cycling", duration=45, date="2025-04-02")

# Leaderboard
Leaderboard.objects.create(user=user1, score=100)
Leaderboard.objects.create(user=user2, score=150)

# Workouts
Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session", duration=60)
Workout.objects.create(name="HIIT", description="High-intensity interval training", duration=30)

print("Test data populated successfully.")

from django.contrib.auth.models import User
from myapp.models import MyModel # type: ignore

# Create a test user
User.objects.create_user(username='testuser', password='password')

# Add test data to MyModel
MyModel.objects.create(field1='value1', field2='value2')

import os
import django
from pymongo import MongoClient

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

# Connect to MongoDB
client = MongoClient('127.0.0.1', 27017)
db = client['octofit_db']

# Example data to insert
data = [
    {"name": "Test User 1", "age": 30},
    {"name": "Test User 2", "age": 25}
]

# Insert data into a collection
collection = db['test_collection']
collection.insert_many(data)

print("Data inserted successfully")