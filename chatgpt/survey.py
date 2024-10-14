class Poll:
    def __init__(self, question, options):
        """Initialize a poll with a question and a list of options."""
        self.question = question
        self.options = options
        self.votes = {option: 0 for option in options}
    
    def vote(self, option):
        """Register a vote for a given option if it exists."""
        if option in self.votes:
            self.votes[option] += 1
        else:
            raise ValueError(f"Option '{option}' is not valid.")
    
    def get_results(self):
        """Return the current results (vote count for each option)."""
        return self.votes


class SurveyPlatform:
    def __init__(self):
        """Initialize the survey platform with an empty list of polls."""
        self.polls = []
    
    def create_poll(self, question, options):
        """Create a new poll with a question and list of options."""
        if len(options) < 2:
            raise ValueError("A poll must have at least two options.")
        poll = Poll(question, options)
        self.polls.append(poll)
        return len(self.polls) - 1  # Return the poll's index
    
    def list_polls(self):
        """List all polls available on the platform."""
        if not self.polls:
            return "No polls available."
        return [
            f"Poll {i}: {poll.question} (Options: {', '.join(poll.options)})"
            for i, poll in enumerate(self.polls)
        ]
    
    def vote_in_poll(self, poll_id, option):
        """Vote in a poll by specifying the poll ID and the option to vote for."""
        if 0 <= poll_id < len(self.polls):
            poll = self.polls[poll_id]
            poll.vote(option)
        else:
            raise ValueError("Invalid poll ID.")
    
    def view_poll_results(self, poll_id):
        """View the results of a poll by poll ID."""
        if 0 <= poll_id < len(self.polls):
            poll = self.polls[poll_id]
            return poll.get_results()
        else:
            raise ValueError("Invalid poll ID.")


# Example interaction (can be turned into a simple console interface or web app)
platform = SurveyPlatform()

# Simulating some actions on the platform
poll_id = platform.create_poll("What is your favorite programming language?", ["Python", "JavaScript", "Java", "C++"])
platform.vote_in_poll(poll_id, "Python")
platform.vote_in_poll(poll_id, "Python")
platform.vote_in_poll(poll_id, "JavaScript")

# Listing polls and viewing results
available_polls = platform.list_polls()
poll_results = platform.view_poll_results(poll_id)

available_polls, poll_results
