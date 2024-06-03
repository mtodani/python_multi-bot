import random #randomモジュールをインポート

# 正解の時に実行される関数を用意
def print_seikai():
    print("!!!!!!!!!!正解です!!!!!!!!!!")

# 不正解の時に実行される関数を用意
def print_fuseikai(dayOfWeek):
    print("残念！不正解です！！")
    print("答えは",dayOfWeek,"です。")


#機能が呼び出される時のために関数 english_quiz()を用意
def english_quiz():
    print("-----------------------------------------")
    print("日曜日～土曜日までランダムで出されていきます")

    while True: #無限ループをさせる

        # 各曜日をリストyoubiに格納
        youbi = ["日曜日","月曜日","火曜日","水曜日","木曜日","金曜日","土曜日"]
        # リストyoubiの中からランダムに一つ選んで、random_youbiに代入
        random_youbi = random.choice(youbi)

        print("-----------------------------------------")
        print(random_youbi,"を英語で答えてください")
        print("（終了して、メニューに戻る場合は「0」を入力）")

        kotae = input("入力：") #答え、または「0」を入力させて変数kotaeに代入

        if random_youbi == youbi[0]: #もしrandom_youbiがリストyoubiの０番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Sunday" もしくは　"sunday" もしくは　"SUNDAY"の場合
            elif kotae == "Sunday" or kotae == "sunday" or kotae == "SUNDAY":
                #正解時に実行する関数を呼び出す
                print_seikai() 

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Sunday")
                

        elif random_youbi == youbi[1]: #そうでなければ、もしrandom_youbiがリストyoubiの1番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Monday" もしくは"monday" もしくは"MONDAY"の場合
            elif kotae == "Monday" or kotae == "monday" or kotae == "MONDAY":
                #正解時に実行する関数を呼び出す
                print_seikai() 

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Monday")

        elif random_youbi == youbi[2]: #そうでなければ、もしrandom_youbiがリストyoubiの2番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Tuesday" もしくは"tuesday" もしくは"TUESDAY"の場合
            elif kotae == "Tuesday" or kotae == "tuesday" or kotae == "TUESDAY":
                #正解時に実行する関数を呼び出す
                print_seikai() 

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Tuesday") 

        elif random_youbi == youbi[3]: #そうでなければ、もしrandom_youbiがリストyoubiの3番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Wednesday" もしくは"wednesday" もしくは"WEDNESDAY"の場合
            elif kotae == "Wednesday" or kotae == "wednesday" or kotae == "WEDNESDAY":
                #正解時に実行する関数を呼び出す
                print_seikai()

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Wednesday")

        elif random_youbi == youbi[4]: #そうでなければ、もしrandom_youbiがリストyoubiの4番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Thursday" もしくは"thursday" もしくは"THURSDAY"の場合
            elif kotae == "Thursday" or kotae == "thursday" or kotae == "THURSDAY":
                #正解時に実行する関数を呼び出す
                print_seikai() 

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Thursday")    

        elif random_youbi == youbi[5]: #そうでなければ、もしrandom_youbiがリストyoubiの5番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Friday" もしくは"friday" もしくは"FRIDAY"の場合
            elif kotae == "Friday" or kotae == "friday" or kotae == "FRIDAY":
                 #正解時に実行する関数を呼び出す
                print_seikai()

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Friday")


        elif random_youbi == youbi[6]: #そうでなければ、もしrandom_youbiがリストyoubiの6番目と同じ場合

            if kotae == "0": #ifをネストし、kotaeが0の場合、
                break        #無限ループを終了させる

            #そうでなければ、もし、kotaeが"Saturday" もしくは"saturday" もしくは"SATURDAY"の場合
            elif kotae == "Saturday" or kotae == "saturday" or kotae == "SATURDAY":
                #正解時に実行する関数を呼び出す
                print_seikai() 

            else: #そうでない場合
                #不正解時に実行する関数を実行
                print_fuseikai("Saturday")
