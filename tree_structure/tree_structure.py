"""木構造での探索"""
#円と線を使って階層構造の分岐を表現する方法は、木の上下を逆さまにして枝が伸びているように見えることから「木構造」と呼ばれている。また、円（接点）をノード、線（辺、枝）をエッジという。
#リストに格納されている単純なデータを探索する場面だけでなく、階層構造になっているデータを探索する場面を考える。
#コンピュータのフォルダ内に保存されているファイルを探す場合など、その探索方法は大きく分けて2つの探索方法がある。幅優先探索と深さ優先探索である。
"""幅優先探索"""
#探索を開始するところから近いものをリストアップし、さらにそれぞれ細かく調べて行く方法を幅優先探索という。
#例えば、本を読むときに目次を見て全体を把握し、さらにそれぞれの章について概要を読み、さらに内容を読む、といったイメージである。求める条件に合致するものを1つだけ得られれば良く、見つかった時点で処理を終了できる場合には高速に処理できる。
"""深さ優先探索"""
#目的の方へ勧めるだけ進んで、勧めなくなったら戻る方法を深さ優先探索と呼ぶ。「バックトラック」とも呼ばれ、全ての答えを見つけるときにはよく使われる。
#再帰処理が使われることが多く、オセロや将棋、以後などの対戦型のゲーム探索を行う場合などには必須の探索方法である。
#全ての答えを見つけなくても、決められた深さまで探索する。という使い方でもよく使われる。
#深さ優先探索には、全てのノードを処理する順番として、行きがけ順、通りがけ順、帰りがけ順がある。ノードに示されている番号の小さいほうから順に処理していく。

#全ての答えを求める必要がある場合、幅優先探索では、探索途中のノードを全て保持しておく必要があるが、深さ優先探索では現在のノードを保持しておくだけで処理を進められる。つまり、幅優先探索よりも深さ優先探索の方がメモリ使用量を抑えることができる。

#一方で、最短でたどり着けるものを1つだけ見つける場合には、見つかった時点での処理を終了できる幅優先探索の方が高速である。（深さ優先探索では、全てのノードを調べてから最短かどうか判定する必要がある。）

#それぞれの特徴を理解して、問題にあった手法を選ぶ必要がある。
