from tkinter import *

window=Tk()
window.title("Conver Roman Nums")

romannum = Label(text="enter roman nums :")
romannum.grid(row=0,column=0)

romannum_entry=Entry()
romannum_entry.grid(row=0,column=1)


result= Label(text="enter")
result.grid(row=1,column=1)

def convert_romanNum():
    Rn=romannum_entry.get()
    global result
    if Rn == "":

        result.config(text="enter romen num to convert!!")
    else:
        try:

            if "I" in Rn and "V" not in Rn and "X" not in Rn and "L" not in Rn and "C" not in Rn and len(Rn) <= 3 and "M" not in Rn and "D" not in Rm:
                result.config(text=len(Rn)*1)

            elif Rn == "IV":
                result.config(text="4")

            elif Rn == "V":
                result.config(text="5")

            elif "V" and "I" in Rn and "X" not in Rn and len(Rn)<=4 and Rn.count("V")<=1 and Rn.count("I")<=3 and "L" not in Rn and "C" not in Rn and "D" not in Rn and "M" not in Rn:
                result.config(text=5 + len(Rn)-1)








            elif Rn.count("X")<=4 and Rn.count("I")<=3 and Rn.count("V")<=1 and Rn.count("IV")<=1 and Rn.count("IX")<=1 and "L" not in Rn and "C" not in Rn and "D" not in Rn and "M" not in Rn:
                result.config(text=Rn.count("X")*10 + Rn.count("V")*5 + Rn.count("I")*1 - Rn.count("IX")*2 - Rn.count("IV")*2)

            elif Rn.count("L") <= 1 and Rn.count("X")<=4 and Rn.count("I")<=3 and Rn.count("V")<=1 and Rn.count("IV")<=1 and Rn.count("IX")<=1 and Rn.count("XL")<=1 and "C" not in Rn and "D" not in Rn and "M" not in Rn:
                result.config(text=Rn.count("L")*50 + Rn.count("X")*10 + Rn.count("V")*5 + Rn.count("I")*1 - Rn.count("IX")*2 - Rn.count("IV")*2 - Rn.count("XL")*20)

            elif Rn.count("C")<=3 and Rn.count("L") <= 1 and Rn.count("X")<=4 and Rn.count("I")<=3 and Rn.count("V")<=1 and Rn.count("IV")<=1 and Rn.count("IX")<=1 and Rn.count("XL")<=1 and Rn.count("XC")<=1 and "D" not in Rn and "M" not in Rn:
                result.config(text=Rn.count("C")*100 + Rn.count("L")*50 + Rn.count("X")*10 + Rn.count("V")*5 + Rn.count("I")*1 - Rn.count("IX")*2 - Rn.count("IV")*2 - Rn.count("XL")*20 - Rn.count("XC")*20)

            elif Rn.count("D")<=1 and Rn.count("C")<=3 and Rn.count("L") <= 1 and Rn.count("X")<=4 and Rn.count("I")<=3 and Rn.count("V")<=1 and Rn.count("IV")<=1 and Rn.count("IX")<=1 and Rn.count("XL")<=1 and Rn.count("XC")<=1 and Rn.count("CD")<=1 and "M" not in Rn:
                result.config(text=Rn.count("D")*500 + Rn.count("C")*100 + Rn.count("L")*50 + Rn.count("X")*10 + Rn.count("V")*5 + Rn.count("I")*1 - Rn.count("IX")*2 - Rn.count("IV")*2 - Rn.count("XL")*20 - Rn.count("XC")*20 - Rn.count("CD")*200)

            elif Rn.count("M")<=5 and Rn.count("D")<=1 and Rn.count("C")<=4 and Rn.count("L") <= 1 and Rn.count("X")<=4 and Rn.count("I")<=3 and Rn.count("V")<=1 and Rn.count("IV")<=1 and Rn.count("IX")<=1 and Rn.count("XL")<=1 and Rn.count("XC")<=1 and Rn.count("CD")<=1 and Rn.count("CM")<=1:
                result.config(text=Rn.count("M")*1000 + Rn.count("D")*500 + Rn.count("C")*100 + Rn.count("L")*50 + Rn.count("X")*10 + Rn.count("V")*5 + Rn.count("I")*1 - Rn.count("IX")*2 - Rn.count("IV")*2 - Rn.count("XL")*20 - Rn.count("XC")*20 - Rn.count("CD")*200 - Rn.count("CM")*200)

            else:
                result.config(text="enter romen num to convert!!")

            '''
            if Rn == "I":

                result.config(text="1")
            elif Rn == "II":
                result.config(text="2")
            elif Rn == "III":
                result.config(text="3")
            elif Rn == "IV":
                result.config(text="4")
            elif Rn == "V":
                result.config(text="5")
            '''



        except:
            result.config(text="enter romen num to convert!!")



conver_button=Button(text="Convert roman numbers",command=convert_romanNum)
conver_button.grid(row=1,column=0)




window.mainloop()

