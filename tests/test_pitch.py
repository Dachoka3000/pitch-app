rom app.models import User,Comment,Pitch
from app import db
import unittest

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.pitch = Pitch(pitchword="There are no feelings in business", cat_id=1,user_id=1)  )