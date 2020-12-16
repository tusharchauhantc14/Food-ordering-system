import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os


def Text_to_speech(Message):
    speech = gTTS(text=Message, slow=False, lang="en")
    speech.save('D:\\orderingvoice.mp3')
    playsound('D:\\orderingvoice.mp3')
    os.remove('D:\\orderingvoice.mp3')


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:" + str(e))

    return said


def get_num(a):
    speech_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                  '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    text_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30]
    if a in speech_num:
        c = speech_num.index(a)
        d = text_num[c]
    return d


pizza1 = "Peppy Paneer";
pizza2 = "Chicken Bar BQ";
pizza3 = "Peri Peri";
pizza4 = "Creamy Max"
roll1 = "Chicken Chatni Roll";
roll2 = "Paneer Makhani Roll";
roll3 = "Veg Roll With Fries"
bur1 = "Zinger Burger";
bur2 = "Chicken Burger";
bur3 = "king Burger"
sand1 = "Club Sandwich";
sand2 = "Chicken Crispy Sandwich";
sand3 = "Extream Veg Sandwich"
bir1 = "Chicken Biryani";
bir2 = "Veg Biryani";
bir3 = "Deluxe Biryani"
choice = 0;
gotostart = "yes"

while gotostart == "yes":

    print(
        "\t\t--------------------------------------------------Indian Fast Food Center-------------------------------------------------------\n\n")
    print("Please Enter Your Name: ")
    Text_to_speech("Please Enter Your Name: ")
    name = get_audio()
    print("Hello {}\n\nWhat would you like to order?\n\n".format(name))
    Text_to_speech("Hello {}\n\nWhat would you like to order?\n\n".format(name))

    print("\t\t\t\t--------Menu--------\n\n")

    Text_to_speech("enter 1 for pizzas 2 for burgers 3 for sandwich 4 for rolls 5 for biryani")
    print("1) Pizzas\n")
    print("2) Burgers\n")
    print("3) Sandwich\n")
    print("4) Rolls\n")
    print("5) Biryani\n\n")
    choice = get_audio()

    if "1" in choice:
        Text_to_speech("Please select Your flavour")
        print("\n1){}\n".format(pizza1))
        print("2){}\n".format(pizza2))
        print("3){}\n".format(pizza3))
        print("4){}\n".format(pizza4))

        Text_to_speech("enter 1 for {} 2 for {} 3 for {} 4 for {}".format(pizza1, pizza2, pizza3, pizza4))
        # Text_to_speech("{}".format(pizza1)); Text_to_speech("{}".format(pizza2)); Text_to_speech("{}".format(pizza3)); Text_to_speech("{}".format(pizza4))
        Text_to_speech("Please Enter Your choice from 1to4")
        a = get_audio()
        pchoice = get_num(a)  # get_audio()

        if pchoice >= 1 and pchoice <= 5:
            print("\n1) Small Rs.250\n2) Regular Rs.500\n3) Large Rs.900\n")
            Text_to_speech("please select pizza size 1Small Rs250 2Regular Rs500 3Large Rs900")
            Text_to_speech("Please Enter Your choice from 1to3")
            a = get_audio()
            pchoice1 = get_num(a)  # get_audio()

            if pchoice1 >= 1 and pchoice1 <= 3:
                Text_to_speech("Please Enter quantity")
                a = get_audio()
                quantity = get_num(a)  # get_audio()

                if pchoice1 == 1:
                    choice = 250 * quantity


                elif pchoice1 == 2:
                    choice = 500 * quantity


                elif pchoice1 == 3:
                    choice = 900 * quantity

        if pchoice == 1:
            print("\t\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, pizza1))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\n\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice == 2:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, pizza2))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice == 3:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, pizza3))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice == 4:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, pizza4))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        Text_to_speech("Would you like to order anything else please enter yes or no")
        gotostart = get_audio()










    elif "2" in choice:

        print("\n1 {} Rs.180\n".format(bur1))
        print("2 {} Rs.150\n".format(bur2))
        print("3 {} Rs.160\n".format(bur3))
        Text_to_speech("1 {} Rs180. 2 {} Rs150. 3 {} Rs160".format(bur1, bur2, bur3))
        Text_to_speech("Please Enter Your choice from 1to3")
        a = get_audio()
        pchoice1 = get_num(a)

        if pchoice1 >= 1 and pchoice1 <= 3:
            Text_to_speech("Please Enter quantity")
            a = get_audio()
            quantity = get_num(a)

            if pchoice1 == 1:
                choice = 180 * quantity

            elif pchoice1 == 2:
                choice = 150 * quantity


            elif pchoice1 == 3:
                choice = 160 * quantity

        if pchoice1 == 1:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, bur1))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center \n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 2:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, bur2))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Carl's Jr. Pizza\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 3:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, bur3))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        Text_to_speech("Would you like to order anything else please enter yes or no")
        gotostart = get_audio()





    elif "3" in choice:
        print("\n1) {} Rs.240\n".format(sand1))
        print("2) {} Rs.160\n".format(sand2))
        print("3) {} Rs.100\n".format(sand3))
        Text_to_speech("1 {} Rs240. 2 {} Rs160. 3 {} Rs100".format(sand1, sand2, sand3))
        Text_to_speech("Please Enter Your choice from 1to3")
        a = get_audio()
        pchoice1 = get_num(a)

        if pchoice1 >= 1 and pchoice1 <= 3:
            Text_to_speech("Please Enter quantity")
            a = get_audio()
            quantity = get_num(a)

            if pchoice1 == 1:
                choice = 240 * quantity


            elif pchoice1 == 2:
                choice = 160 * quantity


            elif pchoice1 == 3:
                choice = 100 * quantity

        if pchoice1 == 1:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, sand1))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 2:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, sand2))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 3:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, sand3))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        Text_to_speech("Would you like to order anything else please enter yes or no")
        gotostart = get_audio()



    elif "4" in choice:
        print("\n1) {} Rs.150\n".format(roll1))
        print("2) {} Rs.100\n".format(roll2))
        print("3) {} Rs.120\n".format(roll3))
        Text_to_speech("1 {} Rs150. 2 {} Rs100. 3{} Rs120".format(roll1, roll2, roll3))
        Text_to_speech("Please Enter Your choice from 1to3")
        a = get_audio()
        pchoice1 = get_num(a)

        if pchoice1 >= 1 and pchoice1 <= 3:
            Text_to_speech("Please Enter quantity")
            a = get_audio()
            quantity = get_num(a)

            if pchoice1 == 1:
                choice = 150 * quantity


            elif pchoice1 == 2:
                choice = 100 * quantity


            elif pchoice1 == 3:
                choice = 120 * quantity

        if pchoice1 == 1:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, roll1))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 2:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, roll2))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 3:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, roll3))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        Text_to_speech("Would you like to order anything else please enter yes or no")
        gotostart = get_audio()




    elif "5" in choice:
        print("\n1) {} Rs.160\n".format(bir1))
        print("2) {} Rs.220\n".format(bir2))
        print("3) {} Rs.140\n".format(bir3))
        Text_to_speech("1 {} Rs160. 2 {} Rs220. 3 {} Rs140".format(bir1, bir2, bir3))
        Text_to_speech("Please Enter Your choice from 1to3")
        a = get_audio()
        pchoice1 = get_num(a)

        if pchoice1 >= 1 and pchoice1 <= 3:
            Text_to_speech("Please Enter quantity")
            a = get_audio()
            quantity = get_num(a)

            if pchoice1 == 1:
                choice = 160 * quantity


            elif pchoice1 == 2:
                choice = 220 * quantity


            elif pchoice1 == 3:
                choice = 140 * quantity

        if pchoice1 == 1:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, bir1))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center \n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 2:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, bir2))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        elif pchoice1 == 3:
            print("\t\t--------Your Order---------\n")
            print("{} {}".format(quantity, bir2))
            print("\nYour Total Bill is {}\nYour Order Will be delivered in 40 Minutes".format(choice))
            print("\nThank you For Ordering From Indian Fast Food Center\n")
            Text_to_speech(
                "Your Total Bill is {}\nYour Order Will be delivered in 40 Minutes. Thank you For Ordering From Indian Fast Food Center".format(
                    choice))

        Text_to_speech("Would you like to order anything else please enter yes or no")
        gotostart = get_audio()


    else:
        Text_to_speech("Please Select Right Option. Would you like to start the program again please enter yes or no")
        print("Please Select Right Option:\n Would you like to start the program again please enter yes or no")
        gotostart = get_audio()

Text_to_speech("Thanks for eating with us. Have a nice day")
print("\nThanks for eating with us...Have a nice day :)")
