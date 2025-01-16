import math # math sınıfını çağırma

def calculator(): # kullanacağımız sınıfı oluşturma
    while True:
        print("\n--- Hesap Makinesi ---")
        print("1. Toplama (+)")
        print("2. Çıkarma (-)")
        print("3. Çarpma (*)")
        print("4. Bölme (/)")                   # seçenekleri belirtme
        print("5. Karekök (sqrt)")
        print("6. Üs Alma (power)")
        print("7. Çıkış (exit)")

        operation = input("Bir işlem seçin: ")# kullanıcıdan hangi işlemi yapacakları sorulur

        if operation == "exit" or operation == "7": #çıkış işlemleri
            print("Hesap makinesi kapatıldı.") # hesap makinesinin kapatıldığını kullanıcıya belirtme
            break #hesap makinesini kapatma

        #karekök için yalnızca bir sayı alınması gerektiği durum
        if operation == "sqrt" or operation == "5": #karekök alma işlemleri
            num = float(input("Sayıyı girin: "))# karekök alınacak sayıyı girme
            print(f"Karekök({num}) = {math.sqrt(num)}") # math sınıfındaki sqrt fonksiyonunu kullanarak karekök alma

        # Diğer işlemler için iki sayı alınması
        else:
            num1 = float(input("Birinci sayıyı girin: "))# birinci sayıyı alma
            num2 = float(input("İkinci sayıyı girin: ")) # ikinci sayıyı alma

            if operation == "+" or operation == "1": # kullanıcı toplama işlemini yapmak isterse
                print(f"Sonuç: {num1} + {num2} = {num1 + num2}") # iki sayının toplamını ekrana yazdırma
            elif operation == "-" or operation == "2": # kullanıcı çıkarma işlemini yapmak isterse
                print(f"Sonuç: {num1} - {num2} = {num1 - num2}") # iki sayının farkını ekrana yazdırma
            elif operation == "*" or operation == "3": # kullanıcı çarpma işlemini yapmak isterse
                print(f"Sonuç: {num1} * {num2} = {num1 * num2}") # iki sayının çarpımını ekrana yazdırma
            elif operation == "/" or operation == "4": # kullanıcı bölme işlemini yapmak isterse
                if num2 == 0: #eğer kullanıcı ikinci sayıyı 0 olarak seçerse 
                    print("Hata: Sıfıra bölme tanımsız!") # hiçbir sayı sıfıra bölünemediği için hesap makinesini kapatma
                else:
                    print(f"Sonuç: {num1} / {num2} = {num1 / num2}") # iki sayının bölümünü ekrana yazdırma
            elif operation == "power" or operation == "6": # kullanıcı üs almak isterse
                print(f"Sonuç: {num1} ^ {num2} = {math.pow(num1, num2)}") # math sınıfındaki power fonksiyonunu kullanarak iki sayının üssünü ekrana yazdırma
            else:
                print("Geçersiz işlem seçimi. Lütfen tekrar deneyin.") # kullanıcı herhangi bir işlemin seçeneğini seçmezse hesap makinesini kapatır

calculator() # oluşturduğumuz fonksiyonu çalıştırma (bu fonksiyonu yazmazsak hiçbir şey olmaz)


        
