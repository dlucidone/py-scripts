from random import randint

class player:
    player_name = "Bot"
    player_prizes = 0
    player_money = 10
    def set_player_details(self,name, prizes, money):

        self.player_name = name
        self.player_prizes = prizes
        self.player_money = money

    def get_player_details(self):

        print("Name:{}\nPrizes:{}\nMoney:{}".format(self.player_name, self.player_prizes, self.player_money))



class lucky_number_generator:

    def generate_number(self):
        self.lucky_number = randint(1, 5)
        #return lucky_number



class Game(player, lucky_number_generator):

    def __init__(self):
        pass


GameObj = Game()

#new_money=0
Choice = True
while Choice == True:
                print("(1) Set Up New Player\n"
                      "(2) Guess A Prize \n"
                      "(3) What Have I Won So Far?\n"
                      "(4) Display Game Help\n"
                      "(5) Exit Game\n")
                try:
                    choice = int(input("Select an option : "))
                except:
                  print("Enter Integer")
                  continue

                if choice == 1:
                        print("Enter Player details")
                        try:
                            name = input("Enter player name :" )
                        except:
                            print("Error:Enter String for name|Try Again")
                            continue
                        try:
                            prizes = int(input("Enter No. of Prizes : "))
                        except:
                            print("Error:Enter Number for Prizes|Try Again ")
                            continue
                        try:
                            money = float(input("Enter Total money player has : "))

                            if money<5:
                                print("Enter Money Greater than 5 To Play")
                                continue
                        except:
                            print("Error:Enter Number in Money|Try Again")
                            continue
                        GameObj.set_player_details(name,prizes,money)
                        fw = open('Player_Record.txt', 'w')
                        fw.write(GameObj.player_name)
                        fw.write("\n")
                        fw.write(str(GameObj.player_prizes))
                        fw.write("\n")
                        fw.write(str(GameObj.player_money))
                        fw.close()
                        continue





                elif choice == 2:
                    '''print ("Do You want to enter Game - Press Y to Continue or No to Main Menu ")
                    choice_for_game = str(input())
                    if choice_for_game  == "Y" or "y":
                        print("Lets Start the game")
                        break
                    elif choice_for_game == "N" or "n":
                        continue
                    else:
                        print ("Enter a valid response")'''
                    print("Lets Roll the ball")
                    print("Guess a Number Based Upon the List and It Should Be in Range[1-5]")

                    try:
                        Guess_Number = int(input())
                    except:
                        print("Enter Integer")
                        continue

                    GameObj.generate_number()



                    if Guess_Number<=5 and Guess_Number == GameObj.lucky_number:
                        print("You Selected Number {} and LuckyNumberGenerated is {}".format(Guess_Number,GameObj.lucky_number))
                        print("You Won",Guess_Number*10)
                        new_money = GameObj.player_money
                        new_money += Guess_Number*10-Guess_Number
                        #print(new_money)
                        print("new money",new_money)
                        GameObj.player_money=new_money
                        GameObj.player_prizes += 1
                        fw = open('Player_Record.txt', 'w')
                        fw.write(GameObj.player_name)
                        fw.write("\n")
                        fw.write(str(GameObj.player_prizes))
                        fw.write("\n")
                        fw.write(str(GameObj.player_money))
                        fw.close()
                        print("New Score Updated")
                        GameObj.get_player_details()

                        if Guess_Number == 1:
                            print("And You-Won a Pen")

                        elif Guess_Number == 2:
                            print("And You-Won a Book")

                        elif Guess_Number == 3:
                            print("And You-Won a DVD")

                        elif Guess_Number == 4:
                            print("And You-Won a Mouse")

                        elif Guess_Number == 5:
                            print("And You-Won a Keyboard")

                    elif Guess_Number>=6:
                        print("Enter number in Range")

                    else:
                        print("You Selected Number {} and LuckyNumberGenerated is {}".format(Guess_Number,GameObj.lucky_number))
                        print("You Loose",Guess_Number)
                        new_money = GameObj.player_money

                        new_money -= Guess_Number
                        print("new money",new_money)
                        GameObj.player_money=new_money
                        #print(new_money)
                        fw = open('Player_Record.txt', 'w')
                        fw.write(GameObj.player_name)
                        fw.write("\n")
                        fw.write(str(GameObj.player_prizes))
                        fw.write("\n")
                        fw.write(str(GameObj.player_money))
                        fw.close()
                        print("New Score")
                        GameObj.get_player_details()




                elif choice == 3:
                        GameObj.get_player_details()



                elif choice == 4:
                    print("Help center")
                    fw = open('Game_help.txt', 'w')
                    fw.write('''
                    Lucky Vending Machine Game:
                    1 - Default Player Details

                    Name = Bot
                    Prizes = 0
                    Money = 10$

                    2 - Enter Number between 1-5 to play
                    3 - Single Instance Program
                    Number_Generated|Price_Won|Price_Worth|Cost_to_Player\n
                    =======================================================
                     1\t\t\tPen      \t\t\t$10\t\t\t$1
                     2\t\t\tBook     \t\t\t$20\t\t\t$2
                     3\t\t\tDVD      \t\t\t$30\t\t\t$3
                     4\t\t\tMouse    \t\t\t$40\t\t\t$4
                     5\t\t\tKeyboard \t\t\t$50\t\t\t$5
                    ''')

                    fw.close()
                    fr = open('Game_help.txt', 'r')
                    text = fr.read()
                    print(text)
                    fr.close()


                elif choice == 5:
                        exit(0)



                else:
                    print("Enter a Valid Choice")
                    continue

