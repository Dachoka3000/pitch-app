rom app.models import User,Comment,Pitch
from app import db
import unittest

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.pitch = Pitch(pitchword="There are no feelings in business", cat_id=1,user_id=1)  )
        self.comment = Comment(commentword = 'nice', pitch_id=1, user_id=1)

    def tearDown(self):
        self.comment.query.delete()
        self.pitch.query.delete()

    def test_comment_instance(self):
        self.assertEquals(self.comment.comment,'nice')
        self.assertEquals(self.comment.pitch,self.pitch)

    def test_save(self):
        self.comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment(self):
        self.comment.save_comment()
        get=Comment.get_comments(self.pitch.id)
        self.assertTrue(len(get)==1)