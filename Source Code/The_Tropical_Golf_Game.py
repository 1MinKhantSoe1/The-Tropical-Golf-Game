import random


def play_golf(meters, par, list_of_score, overall):
    """ start playing the game in this function"""

    original_par = par
    shot = 0
    count = 0
    total_meters = meters
    result = ""

    while total_meters > 0:
        """ this loop is start until the ball is not in the hole"""

        driver = random.randint(80, 120)  # this will give us random number between 80 to 120
        iron = random.randint(24, 36)  # this will give us random number between 24 to 36
        putter = random.randint(8, 12)  # this will give us random number between 8 to 12

        print("You are {0:.0f}m from the hole, after {1} shot/s.".format(total_meters, shot))
        print("Club selection: press D for driver, I for Iron, P for Putter.")
        club = input("Choose club: ")

        if club.upper() == "D":  # for driver process

            total_meters = abs(total_meters - driver)
            print("\nYour shot went {0:.0f}m.".format(driver))
            shot += 1

            if shot > par:
                count += 1

        elif club.upper() == "I":  # for iron process

            total_meters = abs(total_meters - iron)
            print("\nYour shot went {0:.0f}m.".format(iron))
            shot += 1

            if shot > par:
                count += 1

        elif club.upper() == "P":  # for putter process

            if total_meters <= 10:  # when total meter is under 10 this condition will work

                random_dis_for_putter = random.randint(80, 120)
                shot_went = total_meters * random_dis_for_putter // 100  # 80% and 120% of the shot

                if shot_went == 0:
                    shot_went = 1

                total_meters = abs(total_meters - shot_went)
                print("\nYour shot went {0:.0f}m.".format(shot_went))
                shot += 1

                if shot > par:
                    count += 1

            else:  # when total meter is 10m above this condition will work

                total_meters = abs(total_meters - putter)
                print("\nYour shot went {0:.0f}m.".format(putter))
                shot += 1

                if shot > par:
                    count += 1

        else:

            print("\nInvalid club selection – air swing :(\n")
            print("Your shot went 0m.")

            shot += 1
            count += 1

    ball_is_in_the_hole(total_meters, shot, par, count, original_par, result, list_of_score, overall)

    return total_meters


def ball_is_in_the_hole(total_meters, shot, par, count, original_par, result, list_of_score, overall):
    """ when the ball is in the hole"""

    overall_score = 0

    if total_meters == 0 and (len(list_of_score) == 0):  # only for 1st round

        if shot > par:

            print("Clunk…After  {0} hits your ball is in the hole!".format(shot))
            print("Disappointing. You are {0} over par for this hole.".format(count))
            overall_score += shot
            print("Your overall score is {0} and you are {1} over par after {2} holes."
                  .format(overall_score, count, str(len(list_of_score) + 1)))

            result = str(shot) + " shots." + " {0} over par".format(count)

        elif shot < par:

            under_shot = original_par - shot

            print("Clunk…After  {0} hits your ball is in the hole!".format(shot))
            print("Congratulations. You are {0} under par for this hole.".format(under_shot))
            overall_score += shot
            print("Your overall score is {0} and you are {1} under par after {2} holes."
                  .format(overall_score, under_shot, str(len(list_of_score) + 1)))

            result = str(shot) + " shots." + " {0} under par".format(under_shot)

        elif shot == par:

            print("Clunk…After  {0} hits your ball is in the hole!".format(shot))
            print("And that's par.")
            overall_score += shot
            print("Your overall score is {0} and you are {1} over par after {2} holes."
                  .format(overall_score, count, str(len(list_of_score) + 1)))

            result = str(shot) + " shots." + " on par"

    elif total_meters == 0:  # for 2nd round and next other round are work in this condition

        previous_shot = 0

        for o in overall:

            previous_shot = o

        if shot > par:

            print("Clunk…After  {0} hits your ball is in the hole!".format(shot))
            print("Disappointing. You are {0} over par for this hole.".format(count))
            overall_score = previous_shot + shot
            print("Your overall score is {0} and you are {1} over par after {2} holes."
                  .format(overall_score, count, str(len(list_of_score) + 1)))

            result = str(shot) + " shots." + " {0} over par".format(count)

        elif shot < par:

            under_shot = original_par - shot

            print("Clunk…After  {0} hits your ball is in the hole!".format(shot))
            print("Congratulations. You are {0} under par for this hole.".format(under_shot))
            overall_score = previous_shot + shot
            print("Your overall score is {0} and you are {1} under par after {2} holes."
                  .format(overall_score, under_shot, str(len(list_of_score) + 1)))

            result = str(shot) + " shots." + " {0} under par".format(under_shot)

        elif shot == par:

            print("Clunk…After  {0} hits your ball is in the hole!".format(shot))
            print("And that's par.")
            overall_score = previous_shot + shot
            print("Your overall score is {0} and you are {1} over par after {2} holes."
                  .format(overall_score, count, str(len(list_of_score) + 1)))

            result = str(shot) + " shots." + " on par"

    list_of_score.append(result)
    overall.append(overall_score)

    return result


def display_result(name, list_of_score):
    """ display the final result when the user quit the game"""
    all_round = 1
    print("\nThanks for playing {0}".format(name))

    for row in list_of_score:
        print("Round {0} : {1}.".format(all_round, row))
        all_round += 1


def display_instruction():
    """ display the instruction to user"""
    print(
        "\nThis is a simple golf game in which each hole is 230m game away with par 5. You "
        "\nare able to choose"
        "from 3 clubs, the Driver, Iron or Putter. The Driver will hit \naround 100m, "
        "the Iron around"
        "30m and"
        "the Putter around 10m. The putter is \nbest used very close to the hole.\n"
        "For each shot, you may use a driver, iron or a putter – each shot will vary in distance.")
    print("The average distance each club can hit is:")
    print("\t Driver = 100m\n\t Iron = 30m\n\t Putter = 10m\n")

    print("Golf!")
    print("(I)nstructions")
    print("(P)lay round")
    print("(Q)uit\n")


def display_option():
    """ display three option for user"""
    print("\n(I)nstructions")
    print("(P)lay round")
    print("(Q)uit\n")


def main():

    overall = []  # list of overall score
    list_of_score = []  # list of all round score

    name = input("What is your name?\n")

    while name == "":
        """ when name is empty """
        print("I'm sorry, you need to fill your name.")

        name = input("What is your name?\n")

    while name != "":
        """ when name is not empty """
        print("Welcome", name)

        print("Let's play golf, CP1401 style!\n")

        try:

            par_for_course = int(input("Choose a par for this course (between 3-5 inclusive)\n"))

            while par_for_course < 3 or par_for_course > 5:
                # when par for course is under 3 or over 5 this loop will start

                par_for_course = int(input("I’m sorry, you must choose a number between 3-5 inclusive."
                                           "Please enter again.\n"))

            while 3 <= par_for_course <= 5:  # par for course is between 3-5

                try:

                    meters_to_the_hole = int(input("How many meters to the hole (between 195 – 250 inclusive)\n"))

                    while meters_to_the_hole < 195 or meters_to_the_hole > 250:

                        meters_to_the_hole = int(input("I’m sorry, you must choose a number between 195-250 inclusive. "
                                                       "Please enter again.\n"))

                    while 195 <= meters_to_the_hole <= 250:

                        display_option()

                        user_choice = input()

                        while user_choice:

                            if user_choice.upper() == "P":

                                print("\nThis hole is a {0}m par {1}.".format(meters_to_the_hole, par_for_course))

                                play_golf(meters_to_the_hole, par_for_course, list_of_score, overall)
                                # now the game is start in this function

                                print("\nGolf!")
                                display_option()  # three options will show in this function

                                user_choice = input()

                            elif user_choice.upper() == "I":

                                display_instruction()  # instruction will display in this function

                                user_choice = input()

                            elif user_choice.upper() == "Q":

                                display_result(name, list_of_score)  # final result will be display in this function
                                break

                            else:

                                print("\nInvalid menu choice.\n")
                                print("Let's play golf, CP1401 style!\n")
                                print("Golf!")
                                display_option()

                                user_choice = input()

                        return user_choice

                    return meters_to_the_hole

                except:

                    print("Meter must be number!\n")

            return par_for_course

        except:

            print("Course must be number!\n")

    return name


if __name__ == '__main__':
    main()

    print("")

    print("Created By Min Khant Soe (HakHak)")

    input("")
