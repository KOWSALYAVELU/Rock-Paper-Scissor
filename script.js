function playGame(userChoice) {
  const choices = ["Rock", "Paper", "Scissors"];
  const computerChoice = Math.floor(Math.random() * 3);
  document.getElementById("computer").innerText =
    "Computer chose: " + choices[computerChoice];

  if (userChoice === computerChoice) {
    document.getElementById("result").innerText = "It's a tie!";
  } else if (
    (userChoice === 0 && computerChoice === 2) ||
    (userChoice === 1 && computerChoice === 0) ||
    (userChoice === 2 && computerChoice === 1)
  ) {
    document.getElementById("result").innerText = "You Win!";
  } else {
    document.getElementById("result").innerText = "You Lose!";
  }
}
