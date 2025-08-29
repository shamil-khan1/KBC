questions=[
    ["01. International Literacy Day is observed on ? ","Sep 8" ,"Nov 28","May 2","Sep 22", 1],
    ["02. The Language of Lakshadweep, a Union Territory of India, is?" ,"Tamil","Hindi","Malayalam","Math", 3],

    ["03. In which group of places the Kumbha Mela is held every twelve years?","AUjjain, Puri, Prayag, Haridwar","Prayag, Haridwar, Ujjain,Nasik","Rameshwaram, Puri, Badrinath, Dwarika","Chittakoot, Ujjain, Prayag, Haridwar",2],

    ["04. Bahubali festival is related to?","Islam","Hinduism","Buddhism","Jainism",4],
    ["05. World Environment Day is observed on?", "June 5", "April 22", "March 22", "May 5", 2],
    ["06. The capital of Lakshadweep is?", "Kavaratti", "Agatti", "Minicoy", "Amini", 1],
    ["07. The festival of Onam is primarily associated with which state?", "Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh", 1],
    ["08. Teacher’s Day in India is celebrated on?", "September 5", "October 2", "January 12", "November 14", 2],
    ["09. The river on which Haridwar is situated is?", "Ganga", "Yamuna", "Godavari", "Narmada", 1],
    ["10. The Sun Temple is located at?", "Konark", "Khajuraho", "Modhera", "Hampi", 3],
    ["11. National Youth Day (India) marks the birth anniversary of?", "Swami Vivekananda", "Mahatma Gandhi", "B. R. Ambedkar", "Sardar Patel", 1],
    ["12. The Rann Utsav is celebrated in which state?", "Gujarat", "Rajasthan", "Maharashtra", "Madhya Pradesh", 1],
    ["13. Pongal is celebrated in?", "Tamil Nadu", "Kerala", "Telangana", "Odisha", 2],
    ["14. The Jagannath Rath Yatra is held in?", "Puri", "Varanasi", "Dwarka", "Ujjain", 4],
    ["15. India’s national emblem is adopted from?", "Lion Capital of Ashoka", "Peacock Throne", "Red Fort", "Qutub Minar", 1],
    ["16. The capital of Himachal Pradesh is?", "Shimla", "Dharamshala", "Mandi", "Kullu", 1],
    ["17. The dance ‘Bharatanatyam’ originated in?", "Tamil Nadu", "Odisha", "Karnataka", "Kerala", 3],
    ["18. The highest civilian award in India is?", "Bharat Ratna", "Padma Vibhushan", "Padma Bhushan", "Padma Shri", 1],
    ["19. International Yoga Day is observed on?", "June 21", "May 1", "August 12", "October 10", 1]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Next Question show on screen is rupee :- {levels[i]}\n\n{questions[i]}")
    print(f"1.{question[1]}                                  2.{question[2]}")
    print(f"3.{question[3]}                                  4.{question[4]}")
    try:
        reply=int(input(f"enter your answer(1-4): \n" ))

    except:
        print("invalid number")
        break

    if(reply==question[-1]):
        print(f"Correct Answer, You Have Won ₹{levels[i]}\n")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
            print("No More Question ThankYou")
            break

    else:
        print("Wrong Answer")
        break

print(f"You Can Take  {money} At Home")
