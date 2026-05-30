from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/greet', methods=['POST'])
def greet():
    member = request.form['Member']
    branch=request.form['Branch']
    sem=request.form['Sem']
    team=request.form['Team']


    return f"""
    <html>
    
    <body style='text-align:center; margin-top:10px; ' >
    <div  id="f" style="width:700px; margin:5px auto;  background:light green; border:5px double #b8860b; text-align:center; box-shadow:0 0 20px rgba(0,0,0,0,0.2);">
     <br>   <img src="/static/bjpeg.jpeg" width="80%" hight="80%">
        <h2 style="color:blue;">🎉 Hackathon Entry pass 🎉</h2>
        <p style=" color:pink;">====================================================================</p><br>
        <div id="s" style="display :inline-block ;  text-align:center; color:black;">
        
        <h4>participants : {member}<br>
        Department : {branch}<br>
        semester : {sem}<br>
        Team name : {team}<br>
        Event :24-hour Innovation challenge<br>
        Venue : BMS college indoor - stadium  <br>
        Date : 🗓️ on june 1 , 2026  <br>
        on - Time : ⏱️ at  10:00 AM <br>
        pass number : BMSCE - CS - 25<br>
        Status : Approved ✅<br></h4></div>
        <p style=" color:pink;">====================================================================</p><br>
        
        <div style="color:black; text-align:center;">
        <h3> Guide lines:</h3>
        <ol style=" display:inline-block; text-align:left;">
            <li>  Laptop is mandatory </li>
            <li>  Internet facilities will be provided </li>
            <li>  Maintain discipline during the event</li>
            
            <li>  Team members must stay till final presentation </li>
            <li>  Be present on time</li></ol>
        <h4> "Code ,Create ,Conquer."</h4></div></div>
    </body>
    </html>
    """

app.run(debug=True)