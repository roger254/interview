class Magic_8_Ball(object):
    def pick_random_response(self):
        """returns a random response from a list"""
        import random
        answers = ["It is certain",
                   "It is decidedly so",
                   "Without a doubt",
                   "Yes definitely",
                   "You may rely on it",
                   "As I see it yes",
                   "Most likely",
                   "Outlook good",
                   "Yes",
                   "Signs point to yes",
                   "Reply hazy try again",
                   "Ask again later",
                   "Better not tell you now",
                   "Cannot predict now",
                   "Concentrate and ask again",
                   "Don't count on it",
                   "My reply is no",
                   "My sources say no",
                   "Outlook not so good", "Very doubtful"]
        random_index = int(len(answers) * random.random())
        return answers[random_index]

    def main(self):
        """ask user for a questions and returns a random response"""
        while True:
            question = input("Ask your question(Type 'quit' to stop the program): ")
            if question == "quit":
                break
            else:
                print("Thinking...")
                print("Thinking...")
                print("Thinking...")
                print("Thinking...")
                response = pick_random_response()
                print(response)
