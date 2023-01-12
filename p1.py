# bondhon
# mill manager project

mil_manager_name=input("Mill manager name: ")
total_mamber=int(input("total mamber koto : "))
full_mill_taka=int(input("Full mill er taka: "))
half_mill_taka=int(input("Half_mill er taka: "))

choice_wifi=input(f"{mil_manager_name} tumi ki khala bill wifi bill niba y/n: ")

if choice_wifi=='y':
    wifi_bill_amount=int(input("ai masher wifi bill koto taka: "))
    khala_bill=int(input("khala bill koto taka:  "))
else:
    current_bill=int(input("Taile current bill to niba. koto niba: "))


extra_amount=int(input("otirikto taka koto asce: "))

current_use='n'
wifi='n'
for k in range(total_mamber):
    # already_payment=0
    sum_payment=0
    name=input("\nEnter mamber name: ")
    total_full_mil=int(input("Enter total full mil : "))
    total_half_mil=int(input("Enter total half mill : "))
    if choice_wifi=='y':
        wifi=input(f"{name} use wifi or not y/n : ")
    else:
        current_use=input(f"{name} use current or not y/n : ")

    payment_submition=int(input(f"Enter total payment Submet step: "))
    print()
    for i in range(payment_submition):
        payment_submition_amount=int(input("Enter Payment amount: "))
        sum_payment+=payment_submition_amount

    print(f"Total payment {sum_payment}")

    if wifi=='n' and current_use=='y':
          total_taka=(total_full_mil*full_mill_taka)+(total_half_mil*half_mill_taka)+current_bill+extra_amount
    elif wifi=='n':
         total_taka=(total_full_mil*full_mill_taka)+(total_half_mil*half_mill_taka)+khala_bill+extra_amount
    elif wifi=='y':
       total_taka=(total_full_mil*full_mill_taka)+(total_half_mil*half_mill_taka)+khala_bill+wifi_bill_amount+extra_amount
   

       
     
    need_total_amount= total_taka-sum_payment
    if need_total_amount<0:
        print(f"\n{name}  pabe {-need_total_amount} taka ")

    elif need_total_amount>0:
              print(f"\n{mil_manager_name} paba {need_total_amount} taka ") 
    else:
        print("\n kono taka paba nah ")
    with open("use.txt",'a') as file:
        print()
        if wifi=='y':
             file.write(f"\n{k+1}.{name} : \n Total full mill = {total_full_mil}\n Total half mill = {total_half_mil}\n Khala bill={khala_bill} \n wifi bill={wifi_bill_amount} \n Extra={extra_amount}")
        elif current_use=='y':
              file.write(f"\n{k+1}.{name} : \n Total full mill = {total_full_mil}\n Total half mill = {total_half_mil}\n  current bill={current_bill} \n Extra={extra_amount}")
        else:
              file.write(f"\n{k+1}.{name} : \n Total full mill = {total_full_mil}\n Total half mill = {total_half_mil}\n Khala bill={khala_bill} \n Extra={extra_amount}")
        
        file.write(f"\n{'-'*30}")
        if need_total_amount<0:
           file.write(f"\ntotal taka={ total_taka} \n{name} apne dicen={sum_payment}\n apne paben = { -need_total_amount}\n")
        else:
            file.write(f"\ntotal taka={ total_taka} \n{name} apne dicen={sum_payment}\nbaki ace = { need_total_amount}\n")
        file.write(f"\n{'-'*30}\n")

