from flask import Flask 
app=Flask(__name__) #flask dasturlash yaratish
# @app.route('/home') # baravzerdagi manzil
# def salom_ber(): 
#     return"maruf semiz"

# @app.route('/salom')
# def alik_ol():
#     return "valekum asslom maruf bolichka"

# @app.route('/bu')
# def maruf_semiz():
#     return "bu flaskni uchinchi sahifsi"
# if __name__=="__main__":
#     app.run(debug=True) #severni ishga tushirishva xatolarni korsatish
# # uy ishi
# @app.route('/alo')
# def maruf():
#     return"Bu oquvchi alochi"
# if __name__=="__main__":
#     app.run(debug=True)
# #2
# @app.route('/contact')
# def aloqa():
#     return"Email: oquvchi@gmail.com | Tel: +998 90 123 45 67"
# if __name__=="__main__":
#     app.run(debug=True)
# #3
# @app.route('/kvadrat/<int:son>')
# def kvadrat(son):
#     natija=son**2
#     return f"son kvatrati {natija}"
# if __name__=="__main__":
#     app.run(debug=True)

# @app.route("/kvadrat/<int:son>")
# def kvadrat(son):
#     natija= son**2
#     return f"Son kvadrati {natija}"

# if __name__ == "__main__": 
#     app.run(debug=True)

# @app.route('/juftmi/<int:son>')
# def kvadrat(son):
#     if son%2==0:
#         return"bu son juft"
#     else:
#         return"bu toq son"
# if __name__ == "__main__":
#     app.run(debug=True)

#uy ishi
#1
@app.route('/raqamlar/<int:son>')
def raqamlar(son):
    if son ==1234:
        return "bu sonlar yigindisi 10 ga teng"
    else:
        return "bu 10 ga teng emas"
if __name__ == "__main__":
    app.run(debug=True)
#2
@app.route('/tugilgan/<yil>')
def tugilgan_yil(yil):
    if yil == 2000:
        return "sizning yoshingiz 25 da"
    else:
        return "sizning yoshingizni bilmayman"
if __name__=="__main__":
    app.run(debug=True)
