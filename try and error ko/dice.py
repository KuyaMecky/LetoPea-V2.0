import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMessageBox

class DiceGame(QWidget):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Petals Around The Rose")
    
    # Create a layout and add 5 dice labels and a score label
    layout = QHBoxLayout()
    self.dice_labels = []
    for i in range(5):
      dice_label = QLabel(self)
      dice_label.setAlignment(Qt.AlignCenter)
      self.dice_labels.append(dice_label)
      layout.addWidget(dice_label)
    self.score_label = QLabel(self)
    layout.addWidget(self.score_label)
    self.setLayout(layout)
    
    # Load the dice images and scale them to 80x80 pixels
    self.dice_images = []
    for i in range(1, 7):
      pixmap = QPixmap("try and error ko/dice{}.png".format(i))
      self.dice_images.append(pixmap.scaled(80, 80))
      
    # Create a button to roll the dice
    roll_button = QPushButton("Roll Dice", self)
    roll_button.clicked.connect(self.rollDice)
    layout.addWidget(roll_button)
    
def rollDice(self):
  # Generate a random number between 1 and 6 for each dice
  dice_rolls = []
  for i in range(5):
    dice_rolls.append(random.randint(1, 6))

  # Calculate the total based on the dice rolls
  total = 0
  for x in dice_rolls:
    if x == 3:
      total += 2
    elif x == 5:
      total += 4
    else:
      pass

  # Update the dice labels with the corresponding images
  for i, dice_label in enumerate(self.dice_labels):
    dice_label.setPixmap(self.dice_images[dice_rolls[i] - 1])

  # Prompt the player for their guess
  guess, ok = QInputDialog.getInt(self, "Petals Around The Rose", "Enter your guess:", min=0, max=12)
  if ok:
    # Update the score if the guess is correct
    if guess == total:
      self.score += 1
    QMessageBox.information(self, "Correct!", "You guessed the secret number correctly!")
    # Update the dice labels with the corresponding images
    for i, dice_label in enumerate(self.dice_labels):
      dice_label.setPixmap(self.dice_images[dice_rolls[i] - 1])
    
    # Display the score
    self.score_label.setText("Score: {}".format(self.score))

if __name__ == "__main__":
  app = QApplication([])
  window = DiceGame()
  window.show()
  app.exec_()