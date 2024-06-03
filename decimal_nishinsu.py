import random #randomモジュールをインポート


#機能が呼び出される時のために関数 decimal_binary()を用意
def decimal_binary():
    print("-----------------------------------------")
    print("1~128の10進数がランダムで出されます")

    while True: #無限ループさせる

        decimal_number = random.randint(1,128)  # 1~128をランダムで出して、decimal_numberに代入

        print("-----------------------------------------")
        print("10進数",decimal_number,"を２進数に変換したら？")
        print("（終了して、メニューに戻る場合は「0」を入力）")

        # decimal_numberを2進数に変換し、
        # 0bが付くので[2:]を付けること2番目の文字（インデックス2）から末尾までの部分文字列を取得。その後、int型に変換し、binary_numberに代入
        binary_number = int(bin(decimal_number)[2:])  

        
        try: #例外が発生するかも知れない処理をtryの中に入れる 

            #答えまたは「0」を入力させる。また、if文の条件で比較する時のためにint型(整数型)に変換し、ansに代入
            ans = int(input("入力："))

            if ans == 0: #もし、ansが0の場合
                break    #無限ループを終了

            elif ans == binary_number: #そうでなければ、もしansがbinary_numberと同じ場合
                print("!!!!!!!!!!正解です!!!!!!!!!!")

            else: #そうでない場合
                print("残念！不正解です！！")
                print("答えは",binary_number,"です!")

        except ValueError: #ValueErrorという例外発生時の処理
            print("-----------------------------------------")
            print("!!!!!!!!!!!!!!!!!!!!")
            print("!!!整数で入力して!!!")
            print("!!!!!!!!!!!!!!!!!!!!")