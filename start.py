#作成したモジュールをそれぞれインポート
import sekaidokei 
import decimal_nishinsu
import hexa_nishinsu
import eigo_quiz


while True: #無限ループさせる
    
    print("-----------------------------------------")
    print("～Menu～")
    print("1：世界時計")
    print("2：10進数から２進数当てクイズ")
    print("3：16進数から２進数当てクイズ")
    print("4：曜日を英語でクイズ")
    print("0：やめて、終了")
    print("-----------------------------------------")


    try: #例外が発生するかもしれない処理をtryの中に入れる

        #どの機能をするか番号を入力させ、if文の条件で比較する時のためにint型(整数型)に変換し、choiceに代入
        choice=int(input("どれをしたいですか：")) 

        if choice < 0 or choice > 4:   #もしchoiceが0未満もしくは、４より大きい場合
            print("-----------------------------------------")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!! 0~4の整数で入力してください!!!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        elif choice == 0: #そうでなければば、もし0の場合
            print("-----------------------------------------")
            print("終了します。\nありがとうございました！")
            print("-----------------------------------------")
            break #無限ループを終了

        elif choice == 1: #そうでなければ、もし1の場合
            print("-----------------------------------------")
            print("かしこまりました、世界時計ですね！")
            sekaidokei.world_time()   #インポートしたモジュールsekaidokeiのworld_time関数を呼び出す

        elif choice == 2: #そうでなければ、もし2の場合
            decimal_nishinsu.decimal_binary()  #インポートしたモジュールdecimal_nishinsuのdecimal_binary関数を呼び出す
        
        elif choice == 3: #そうでなければ、もし3の場合
            hexa_nishinsu.hexa_binary()  #インポートしたモジュールhexa_nishinsuのhexa_binary関数を呼び出す

        elif choice == 4: #そうでなければ、もし4の場合
            eigo_quiz.english_quiz()  #インポートしたモジュールeigo_quizのenglish_quiz関数を呼び出す


    except ValueError: #整数以外が入力され、ValueErrorという例外発生時
        print("-----------------------------------------")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! 0~4の整数で入力してください!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        