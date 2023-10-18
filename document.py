class Document:
    def __init__(self):
        self.content = ""
        self.version = 0
        self.history = []

    def edit(self, user, new_content):
        # Save the previous state to the history
        previous_state = {
            'user': user,
            'content': self.content,
            'version': self.version
        }
        self.history.append(previous_state)

        # Update the content and increment the version
        self.content = new_content
        self.version += 1

    def get_content(self):
        return self.content

    def get_version(self):
        return self.version

    def get_history(self):
        return self.history

    def revert_to_version(self, target_version):
        for entry in reversed(self.history):
            if entry['version'] == target_version:
                self.content = entry['content']
                self.version = entry['version']
                return

# Example Usage
doc = Document()

# User 1 makes changes
doc.edit("User 1", "This is the first edit.")
print(f"Current Version: {doc.get_version()} - Content: {doc.get_content()}")

# User 2 makes changes
doc.edit("User 2", "This is the second edit.")
print(f"Current Version: {doc.get_version()} - Content: {doc.get_content()}")

# User 1 tracks history
history = doc.get_history()
for entry in history:
    print(f"Version {entry['version']} by {entry['user']}: {entry['content']}")

# User 2 reverts to a previous version
target_version = 1
doc.revert_to_version(target_version)
print(f"Reverted to Version {target_version}: {doc.get_content()}")
