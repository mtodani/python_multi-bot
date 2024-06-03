from datetime import datetime #datetimeモジュールをインポート
import pytz #世界各地域のタイムゾーン別の時刻を求めるときにサポートしてくれる外部ライブラリーpytzをインポート（サマータイムにも対応）


#引数として渡されるタイムゾーンに関する情報を取得し現地日時に取得し、表示させる関数を用意
def print_jikoku(chiiki,zone): 
    place = pytz.timezone(zone) #タイムゾーン別に関連する情報を関数で取得し、placeに格納
    place_now = datetime.now(place) #placeに入っているタイムゾーンの情報より、現在の日付と時間を取得し,place_nowに格納
    print("-----------------------------------------")
    # place_nowに格納された情報をもとに、それぞれ月、日、時、分を表示
    print(f"{chiiki}ですね！\n{chiiki}の現在日時は {place_now.month}/{place_now.day} {place_now.hour}:{place_now.minute} です！") 


#機能が呼び出される時のために関数 world_time()を用意
def world_time(): 

    while True: #無限ループさせる
        print("-----------------------------------------")
        print("以下の地域の現在日時を表示できます。")
        print("-----------------------------------------")
        print("1：ロンドン")
        print("2：パリ")
        print("3：モスクワ(ロシア)")
        print("4：中国")
        print("5：日本")
        print("6：オーストラリア、シドニー")
        print("7：アメリカ、ロサンゼルス(LA)")
        print("8：アメリカ、ニューヨーク")
        print("0：終了して、メニューに戻る")
        print("-----------------------------------------")

        try:  #例外が発生するかも知れない処理をtryの中に入れる 

            #どの地域にするか番号を入力させ、if文の条件で比較する時のためにint型(整数型)に変換し、choiceに代入
            choice = int(input("表示したい地域の番号を入力して：")) 
            

            if choice < 0 or choice > 8:   #もしchoiceが０未満、もしくは、８より大きい場合
                print("-----------------------------------------")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("!!!!!0～8の整数で入力してください!!!!!!")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            elif choice == 0: #そうでなければ、もしchoiceが0の場合
                break         #無限ループを終了

            elif choice == 1: #そうでなければ、もしchoiceが1の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("ロンドン","Europe/London") 

            elif choice == 2: #そうでなければ、もしchoiceが2の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("フランス、パリ","Europe/Paris") 

            elif choice == 3: #そうでなければ、もしchoiceが3の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("ロシア、モスクワ","Europe/Moscow") 

            elif choice == 4: #そうでなければ、もしchoiceが4の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("中国","Asia/Shanghai")

            elif choice == 5:  #そうでなければ、もしchoiceが5の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("日本","Asia/Tokyo")
                
            elif choice == 6:  #そうでなければ、もしchoiceが6の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("オーストラリア、シドニー","Australia/Sydney")
                
            elif choice == 7:  #そうでなければ、もしchoiceが7の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("アメリカ、ロサンゼルス(LA)","America/Los_Angeles")

            elif choice == 8:  #そうでなければ、もしchoiceが8の場合
                #地域名とタイムゾーンを引数として、渡し print_jikoku関数に渡す
                print_jikoku("アメリカ、ニューヨーク","America/New_York")


        except ValueError: #ValueErrorという例外発生時の処理
            print("-----------------------------------------")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!!!0～8の整数で入力してください!!!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
