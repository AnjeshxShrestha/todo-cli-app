import unittest
from todo_core import add_todo, mark_done, delete_todo
class TestTodoFunctions(unittest.TestCase):
    def test_add_todo(self):
        todos = []
        todos = add_todo(todos, "Test task")
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['task'], "Test task")
        self.assertFalse(todos[0]['done'])

    def test_mark_done(self):
        todos = [{"task": "Test", "done": False}]
        todos = mark_done(todos, 0)
        self.assertTrue(todos[0]['done'])

    def test_delete_todo(self):
        todos = [{"task": "Test", "done": False}]
        todos = delete_todo(todos, 0)
        self.assertEqual(len(todos), 0)

if __name__ == "__main__":
    unittest.main()
