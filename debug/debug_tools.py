def show_memory(messages):
    print("\n Chat memory\n")
    if len(messages)==0:
        print("memory is empty.\n")
        returm
    for i, msg in enumerate(messages,start=1):
        print(f"Message{i}")
        print(f"Role:{msg['role']}")
        print(f"Content:{msg['content']}")
    print('\n===\n')