import unittest
from main import internal_behaviour, agent_2, agent_1, handle_message
import threading
import subprocess




class TestAgent(unittest.TestCase):
    def test_return_type(self):
        state = {"alphabet": ["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"]}
        self.assertEqual(str, type(internal_behaviour(state)))
        self.assertEqual(bool, type(handle_message("hello")))

    def test_message_handling(self):
        self.assertEqual(handle_message("hello"), True)
        self.assertEqual(handle_message("bye"), False)


class TestApp(unittest.TestCase):
    def test_thread_launch(self):
        threading.Thread(target=agent_2).start()
        threading.Thread(target=agent_1).start()
        self.assertEqual(threading.active_count(), 3)


if __name__ == '__main__':
    unittest.main()
