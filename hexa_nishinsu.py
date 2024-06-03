import random  #randomモジュールをインポート


#機能が呼び出される時のために関数 hexa_binary()を用意
def hexa_binary():
    print("-----------------------------------------")
    print("2桁の16進数がランダムで出されていきます！")
    print("がんばってください！")
    
    while True: #無限ループさせる
        
        #一桁目と二桁目を"0123456789ABCDEF"からランダムに選択し、hexa_shinsuに代入
        hexa_shinsu = random.choice("0123456789ABCDEF") + random.choice("0123456789ABCDEF")
        jushinsu = int(hexa_shinsu, 16)  # 16進数を10進数に変換し、int型に変換し、jushinsuに代入

        # １０進数を２進数に変換。0bが付くので[2:]を付けること2番目の文字（インデックス2）から末尾までの部分文字列を取得
        # intを付けて、整数に変換し、入力される答えと整数同士で比較できるようにする
        binary_number=int(bin(jushinsu)[2:]) 

        print("-----------------------------------------")
        print("16進数",hexa_shinsu,"を2進数に変換したら？")
        print("（終了して、メニューに戻る場合は「0」を入力）")

        try: #例外が発生するかも知れない処理をtryの中に入れる 
            #答え、または「0」を入力させる。if文の条件で比較する時のためにint型(整数型)に変換し、ansに代入
            ans = int(input("入力："))

            if ans == 0: #もし、ansが0の場合
                break    #無限ループを終了

            elif ans == binary_number: #そうでなければ、もしansがbinary_numberと同じの場合
                print("!!!!!!!!!!正解です!!!!!!!!!!")
            
            else: #そうでない場合
                print("残念！不正解です！！")
                print("答えは",binary_number,"です。")

        except ValueError: #ValueErrorという例外発生時の処理
            print("-----------------------------------------")
            print("!!!!!!!!!!!!!!!!!!!!")
            print("!!!整数で入力して!!!")
            print("!!!!!!!!!!!!!!!!!!!!")
