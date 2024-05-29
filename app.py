from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "Kwepo"
#api_key = "a03310048e89221dc881820003f85c38353bcae6e28c545fe190bd109ef5933a"
api_key = "f41283f042c8a365b7800b6d599c2fe220be726ca9e7273303dfd8993e706379"
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
    
    elif text == "^2\*2(\*\d+)?$":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    # elif text == "2*2*2":
    #     response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
    #     #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    # elif text == "2*2*3":
    #     response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
    #     #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    # elif text == "2*2*4":
    #     response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
    #     #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
    # elif text == "2*2*5":
    #     response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
    #     #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])

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
    elif text == "1*1*1*1":
        response = "END Your appointment has been successfully booked. Details will be shared in a short while."    
        #sms.send("Your appointment was booked for Monday at 2pm with Dr. Rachel Mundia, Nairobi West Hospital", [phone_number])
       
        
    else:
        response = "END Invalid input. Try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
