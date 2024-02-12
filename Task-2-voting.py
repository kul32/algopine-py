import time

class OnlineVotingSystem:
    def __init__(self, parties):
        self.parties = parties
        self.votes = {party: 0 for party in parties}

    def display_parties(self):
        print("Parties available for voting:")
        for index, party in enumerate(self.parties, start=1):
            print(f"{index}. {party}")

    def vote(self):
        self.display_parties()
        choice = int(input("Enter the number corresponding to your chosen party: "))
        if 1 <= choice <= len(self.parties):
            selected_party = self.parties[choice - 1]
            self.votes[selected_party] += 1
            print(f"You have successfully voted for {selected_party}!")
        else:
            print("Invalid choice. Please select a valid party.")

    def display_results(self):
        print("Voting has ended. Here are the results:")
        for party, votes in self.votes.items():
            print(f"{party}: {votes} votes")

def main():
    parties = ["Party A", "Party B", "Party C", "Party D"]  # Example parties
    voting_system = OnlineVotingSystem(parties)

    print("Welcome to the Online Voting System")

    # Simulate voting process
    while True:
        print("\n1. Vote")
        print("2. Display Results")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            voting_system.vote()
        elif choice == 2:
            voting_system.display_results()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
