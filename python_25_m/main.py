# 【ルール】
# 対戦方法：DealerとPlayerの1対1の対戦ゲーム
#   i）Playerに2枚のカードを配る（一枚は表示・もう一枚は表示しない）
#   ⅱ）Dealerにも2枚カードを配る（Playerと同様）
#   ⅲ）Playerは、両方のカードを確認する。　
#       合計数値が16より小さい　→　もう一枚必ず引く
#       合計数値が16以上　　　　→　引く(hit)［もう一枚もらう］か引かない（stand）
#                                を決めてコールする。
#       hitのコールの限り、カードを引き続ける
#   ⅳ）Playerが終了後、ディーラも同様にカードを引く
#   ⅴ）同時に開いて21に近いほうが勝ち
#   21の場合はBLACK JACKと表示
#   ※  K・Q・Jは10とカウントする。Aは1または11を選択することが出来る
#   ※ カードが21を超えてしまうと、その時点で負けとなる。
#   ※ 最初に配られた2枚のカードが　”Aと10点札”　で21点が完成していた場合は
#    『BLACK JACK』となりその時点で勝ちとなる。
#   ※ 配当がある場合は、配当は3 to 2（1.5倍）となる。
#   ただし、カジノディーラーもブラックジャックだった場合は引き分けとなる。


# 【拡張機能】
#   1）どちらかが5勝したほうが勝ちで、ゲーム終了とする。
#   2）配当（持ち金をかけられるようにする）
import blackjack

blackjack.BlackJack()
