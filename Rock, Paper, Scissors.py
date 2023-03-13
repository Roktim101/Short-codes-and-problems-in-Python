while True:
    p1_move = input("Player 1, choose your move (Rock, Paper, or Scissors): ").lower()
    p2_move = input("Player 2, choose your move (Rock, Paper, or Scissors): ").lower()

    if p1_move == p2_move:
        print("It's a draw!")
    elif p1_move == "rock" and p2_move == "scissors" or \
            p1_move == "paper" and p2_move == "rock" or \
            p1_move == "scissors" and p2_move == "paper":
        print("Player 1 wins!")
    elif p2_move == "rock" and p1_move == "scissors" or \
            p2_move == "paper" and p1_move == "rock" or \
            p2_move == "scissors" and p1_move == "paper":
        print("Player 2 wins!")
    else:
        print("Invalid move, please choose either Rock, Paper, or Scissors.")

    decision = input("Do you want to play again? (y/n): ").lower()
    if decision == "n":
        break

print("Thanks for playing!")
