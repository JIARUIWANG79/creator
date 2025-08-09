# clean_autogen_files.py
import os

base_dir = "."
keep_files = {
    "1_lab1_autogen_agentchat.ipynb",
    "2_lab2_autogen_agentchat.ipynb",
    "3_lab3_autogen_core.ipynb",
    "4_lab4_autogen_distributed.ipynb",
    "5_lab5_autogen_project.ipynb",
    "agent.py",
    "creator.py",
    "messages.py",
    "tickets.db",
    "world.py",
}

deleted = []

for filename in os.listdir(base_dir):
    full_path = os.path.join(base_dir, filename)

    if filename in keep_files:
        continue  # 保留
    if filename.startswith("__") or filename.endswith(".pyc"):
        continue  # 忽略 __pycache__

    try:
        if os.path.isfile(full_path):
            os.remove(full_path)
            deleted.append(filename)
    except Exception as e:
        print(f"❌ Failed to delete {filename}: {e}")

if deleted:
    print("🗑️ Deleted files:")
    for f in deleted:
        print(f" - {f}")
else:
    print("✅ Nothing to delete.")