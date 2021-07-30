from typing import Dict
import threading
import time
import sys
import random


# General takeaway: If only there was a library to easily implement autonomous agents!
# I've created a workaround using 'while True' to keep agents alive,
# threading to run them simultaneously and global variables as inboxes.

# Unfortunately, I was not able to create an abtract agent upon which I could build further. Instead I hardcoded each agent as a function.
# I'd appreciate some guidance and would be more than happy to re-do the project.

# Function that looks for 'hello' in the message it received
def handle_message(message: str) -> bool:
    if "hello" in message:
        sys.stdout.write("Message identified: " + message + "\n")
        return True
    else:
        return False


# Function that generates the new message to be sent to the other agent
def internal_behaviour(state: Dict) -> str:
    word1, word2 = random.randint(0, 9), random.randint(0, 9)
    word = state.get('alphabet')[word1] + " " + state.get('alphabet')[word2]
    return word


# Unable to abstract this away -> hard coding this feature in every agent to be able to edit global variables
def emit_message(message, outbox):
    outbox = message


########## General representation of an agent ##########
inbox_x = 'initialisation'  # the agent's inbox, a global variable


def agent_x():
    global inbox_x
    state = {}  # agent state, can contain data
    while True:
        handle_message(inbox_x)
        internal_behaviour(state)
        time.sleep(1)


##################################################

# The inbox used in this project for the second agent
inbox = "initial"


# The agent that generates messages and sends them
def agent_1():
    global inbox
    state = {"alphabet": ["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"]}
    while True:
        inbox = internal_behaviour(state)
        time.sleep(2)


# The agent that receives and handles the messages
def agent_2():
    global inbox
    while True:
        handle_message(inbox)
        time.sleep(1)


# Initialising the two agents
if __name__ == '__main__':
    threading.Thread(target=agent_2).start()
    threading.Thread(target=agent_1).start()
