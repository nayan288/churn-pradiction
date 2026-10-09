from flask import Flask,request,render_template
import joblib
import os

BASE = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE, "model.joblib"))

app =Flask(__name__)

@app.route("/",methods=["GET","POST"])
def churndata():
    if request.method == "POST":
        Age = request.form.get("Age")
        Tenure = request.form.get("Tenure")
        UsageFrequency = request.form.get("UsageFrequency")
        SupportCalls = request.form.get("SupportCalls")
        PaymentDelay = request.form.get("PaymentDelay")
        TotalSpend = request.form.get("TotalSpend")
        LastInteraction = request.form.get("LastInteraction")
        new_contract_length = request.form.get("new_contract_length")
        new_SubscriptionType = request.form.get("new_SubscriptionType")
        new_Gender = request.form.get("new_Gender")

        data = [[Age,Tenure,UsageFrequency,SupportCalls,PaymentDelay,TotalSpend,LastInteraction,new_contract_length,new_SubscriptionType,new_Gender]]
        result = model.predict(data)
        if result == 1:
            result = "customer will leave"
        else:
            result = "custumer will continue to use our service"
        return render_template("churndata.html",data=result)
    else:
        return render_template("churndata.html")

if __name__ == "__main__":
    app.run(debug=True)
