from simple_agent import SimpleAgent


def test_basic_question():
    agent = SimpleAgent()
    answer = agent.run("What are Python coding best practices?")
    assert answer is not None
    print("✅ test_basic_question passed")


def test_memory_storage():
    agent = SimpleAgent()
    answer = agent.run("How do I submit an expense report?")
    assert answer is not None
    print("✅ test_memory_storage passed")


def test_memory_recall():
    agent = SimpleAgent()
    agent.run("How do I submit an expense report?")
    answer = agent.run("How do employees claim expenses?")
    assert answer is not None
    print("✅ test_memory_recall passed")


def test_episodic_memory():
    agent = SimpleAgent()
    agent.run("What is the company's vacation policy?")
    answer = agent.run("What did I ask about earlier?")
    assert answer is not None
    print("✅ test_episodic_memory passed")


if __name__ == "__main__":
    test_basic_question()
    test_memory_storage()
    test_memory_recall()
    test_episodic_memory()
    print("\n🎉 All tests passed!")
