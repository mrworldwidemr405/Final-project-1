VOTE_FILE = "votes.txt"

def already_voted(uid):
    try:
        with open(VOTE_FILE) as f:
            for line in f:
                if line.startswith(uid + ","):
                    return True
    except:
        return False
    return False

def save_vote(uid, name):
    with open(VOTE_FILE, "a") as f:
        f.write(f"{uid},{name}\n")

def load_votes():
    try:
        with open(VOTE_FILE) as f:
            return f.read()
    except:
        return "No votes yet."