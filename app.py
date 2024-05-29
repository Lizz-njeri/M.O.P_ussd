from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "Kwepo"
api_key = "f67c169248ae4bf36bdc9e798afed8428dcd3770bf78cf051d4faa752fd8a8a9"
africastalking.initialize(username, api_key)

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    print(phone_number)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)
    sms = africastalking.SMS


    if text == "":
        response = "CON Welcome to M.O.P Health.Which age bracket are you in?\n"
        response += "1. Over 18 years\n"
        response += "2. Below 18 years\n"

    elif text== "1":
        response = "CON Do you have a diagnosis for mental health\n"
        response += "1. Yes\n"
        response += "2.No \n"
    
    elif text== "2":
        response = "CON Do you have a diagnosis for mental health\n"
        response += "1. Yes\n"
        response += "2.No \n"

    elif text =="1*1":
        response = "CON Which mental health condition have you been diagnosed?\n"
        response += "1. Bipolar\n"
        response += "2. Clinical depression\n"
        response += "3. Schizophrenia\n"
        response += "4. Eating disorders\n"
        response += "5. PTSD\n"
        response += "6. Anxiety disorders\n"

    elif text == "1*2":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"

    elif text == "1*2*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "1*2*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "1*2*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "1*2*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "1*2*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
       

    elif text == "2*2":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"

   
    elif text == "2*2*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*2*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*2*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*2*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*2*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])

    elif text =="2*1":
        response = "CON Which mental health condition have you been diagnosed?\n"
        response += "1. Bipolar\n"
        response += "2. Clinical depression\n"
        response += "3. Schizophrenia\n"
        response += "4. Eating disorders\n"
        response += "5. PTSD\n"
        response += "6. Anxiety disorders\n"

    elif text == "1*1*1":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"

    elif text == "1*1*2":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"

    elif text == "1*1*3":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "1*1*4":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "1*1*5":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "1*1*6":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"

    elif text == "1*1*1*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*1*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*1*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*1*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*1*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])


    elif text == "1*1*2*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*2*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*2*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*2*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*2*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])

    elif text == "1*1*3*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*3*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*3*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*3*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*3*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "1*1*4*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*4*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*4*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*4*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*4*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "1*1*5*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*5*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*5*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*5*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*5*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number]) 

    elif text == "1*1*6*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*6*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*6*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*6*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "1*1*6*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])  
    

    elif text == "2*1*1":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "2*1*2":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "2*1*3":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "2*1*4":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "2*1*5":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"
    elif text == "2*1*6":
        response = "CON Which day of the week do you want to book the appointment?\n"
        response += "1. Monday\n"
        response += "2. Tuesday\n"
        response += "3. Wednesday\n"
        response += "4. Thursday\n"
        response += "5. Friday\n"


    elif text == "2*1*1*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*1*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phne_number])
    elif text == "2*1*1*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*1*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*1*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])

    elif text == "2*1*2*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*2*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phne_number])
    elif text == "2*1*2*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*2*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*2*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "2*1*3*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*3*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phne_number])
    elif text == "2*1*3*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*3*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*3*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "2*1*4*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*4*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phne_number])
    elif text == "2*1*4*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*4*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*4*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "2*1*5*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*5*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phne_number])
    elif text == "2*1*5*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*5*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*5*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    
    elif text == "2*1*6*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*6*2":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phne_number])
    elif text == "2*1*6*3":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*6*4":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    elif text == "2*1*6*5":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])








        
    else:
        response = "END Invalid input. Try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
